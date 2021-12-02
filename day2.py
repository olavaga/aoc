position, depth, aim = 0, 0, 0
with open('day2.txt', 'r') as fil:
    for line in fil:
        command, distance = line.split()
        if command == 'forward':
            position += int(distance)
            depth += aim * int(distance)
        elif command == 'down':
            # depth += int(distance)
            aim += int(distance)
        elif command == 'up':
            # depth -= int(distance)
            aim -= int(distance)
        else:
            ...
    print(position, depth, position * depth)
