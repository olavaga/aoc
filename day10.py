from statistics import median

with open('data/day10.txt', 'r') as fil:
    data = fil.read()

def matches(last, found):
    return '({[<'.index(last) == ')}]>'.index(found)

def score(sym):
    match sym:
        case ')':
            return 3
        case ']':
            return 57
        case '}':
            return 1197
        case '>':
            return 25137

error_score = 0
completion_scores = []
for line in data.splitlines():
    line = line.strip()
    stack = []
    incorrect = False

    for sym in line:
        match sym:
            case '{' | '[' | '(' | '<':
                stack.append(sym)
            case '}' | ']' | ')' | '>' if stack and matches(stack[-1],sym):
                stack.pop()
            case _:
                error_score += score(sym)
                incorrect = True
                break

    if not incorrect:
        completion_score = 0

        for sym in stack[::-1]:
            completion_score *= 5
            completion_score += '([[{{{<<<<'.count(sym)

        completion_scores.append(completion_score)

print("P1", error_score)
print("P2", median(completion_scores))
