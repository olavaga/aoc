from day16 import sum_version_numbers, evaluate

def test_type_ID_4():
    assert(sum_version_numbers("D2FE28") == 6)

def test_operator_packet():
    assert(sum_version_numbers("38006F45291200") == 1 + 6 + 2)

def test_operator_packet2():
    assert(sum_version_numbers("EE00D40C823060") == 7 + 2 + 4 + 1)

def test_more_examples():
    assert(sum_version_numbers("8A004A801A8002F478") == 16)
    assert(sum_version_numbers("620080001611562C8802118E34") == 12)
    assert(sum_version_numbers("C0015000016115A2E0802F182340") == 23)
    assert(sum_version_numbers("A0016C880162017C3686B18A3D4780") == 31)

def test_sum():
    # C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
    assert(evaluate("C200B40A82") == 1 + 2)

def test_product():
    # 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
    assert(evaluate("04005AC33890") == 6 * 9)

def test_minimum():
    # 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
    assert(evaluate("880086C3E88112") == min(7, 8, 9))

def test_maximum():
    # CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
    assert(evaluate("CE00C43D881120") == max(7, 8, 9))

def test_less_than():
    # D8005AC2A8F0 produces 1, because 5 is less than 15.
    assert(evaluate("D8005AC2A8F0") == int(5 < 15))

def test_greater_than():
    # F600BC2D8F produces 0, because 5 is not greater than 15.
    assert(evaluate("F600BC2D8F") == int(5 > 15))

def test_not_equal():
    # 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
    assert(evaluate("9C005AC2F8F0") == int(5 == 15))

def test_expression():
    # 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
    assert(evaluate("9C0141080250320F1802104A08") == int(1 + 3 == 2 * 2))

