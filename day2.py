import sys

with open('data/day2.txt', 'r') as fil:
    commands = fil.read().splitlines()

position, depth, aim = 0, 0, 0

for command in commands:
    match command.split():
        case ["forward", distance]:
            position += int(distance)
            depth += aim * int(distance)
            
        case ["down", distance]:
            aim += int(distance)
        
        case ["up", distance]:
            aim -= int(distance)
         
        case _:
            print(f"Error parsing command {command}", file = sys.stderr)
            
print(position, depth, position * depth)
