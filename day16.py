from aocd import data
from dataclasses import dataclass
from functools import reduce

@dataclass
class Packet:
    version_number: int
    typeID: int
    literal: int = None
    subpackets: list = None

    def get_version_numbers(self):
        version_number = self.version_number
        if self.subpackets is not None:
            version_number += sum(p.get_version_numbers() for p in self.subpackets)

        return version_number

    def evaluate(self):
        if self.typeID == 0: # sum
            return sum(p.evaluate() for p in self.subpackets)

        elif self.typeID == 1: # product
            return reduce(lambda a,b: a*b, (p.evaluate() for p in self.subpackets))

        elif self.typeID == 2: # minimum
            return min(p.evaluate() for p in self.subpackets)

        elif self.typeID == 3: # maximum
            return max(p.evaluate() for p in self.subpackets)

        elif self.typeID == 4: # literal
            return self.literal

        elif self.typeID == 5: # greater than
            left, right = self.subpackets
            return int(left.evaluate() > right.evaluate())

        elif self.typeID == 6: # less than
            left, right = self.subpackets
            return int(left.evaluate() < right.evaluate())

        elif self.typeID == 7: # equal to
            left, right = self.subpackets
            return int(left.evaluate() == right.evaluate())

        else:
            raise Exception


def chunkNbits(bits, length):
    return bits[length:], int(bits[:length], 2)

def readLiteralValue(packet):
    number = ""
    group = packet[:5]
    bits_read = 0

    while group[0] == '1':
        number += group[1:5]
        bits_read += 5
        group = packet[bits_read: bits_read + 5]


    return bits_read + 5, int(number + group[1:5], 2)

def parsePacket(BITS):
    BITS, version_numbers = chunkNbits(BITS, 3)
    BITS, typeID = chunkNbits(BITS, 3)
    packet = Packet(version_number = version_numbers, typeID = typeID)

    if typeID == 4:
        skip, lit = readLiteralValue(BITS)
        BITS = BITS[skip:]
        packet.literal = lit

    else:
        BITS, length_type_id = chunkNbits(BITS, 1)
        packet.subpackets = []

        if length_type_id:
            BITS, num_sub_packets = chunkNbits(BITS, 11)

            for _ in range(num_sub_packets):
                BITS, subpacket = parsePacket(BITS)
                packet.subpackets.append(subpacket)

        else:
            BITS, bit_length = chunkNbits(BITS, 15)
            orig_len = len(BITS)

            BITS, subpacket = parsePacket(BITS)
            packet.subpackets.append(subpacket)

            while orig_len - len(BITS) < bit_length:
                BITS, subpacket = parsePacket(BITS)
                packet.subpackets.append(subpacket)

    return BITS, packet

def parse(data):
    BITS=str(bin(int(data.strip(),16))[2:]).rjust(len(data)*4, '0')
    BITS, packet = parsePacket(BITS)
    return packet

def evaluate(data):
    return parse(data).evaluate()

def sum_version_numbers(data):
    packet = parse(data)
    return packet.get_version_numbers()

if __name__ == '__main__':
    print("Part1", sum_version_numbers(data))
    packets = parse(data.strip())
    print("Part2", evaluate(data.strip()))

