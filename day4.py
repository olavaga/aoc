sequence = []
boards = []

with open('day4.txt', 'r') as fil:
    sequence += fil.readline().strip().split(',')
    
    board = []
    for line in fil:
        row = line.split()
        
        if row:
            board.append(row)
        elif board:
            boards.append(board)
            board = []

    if board:
        boards.append(board)
        board = []

wins = []
for board in boards:
    rc = board + [*zip(*board[::-1])]
    first = len(sequence),
    for l in rc:
        ind, last_n = max(map(lambda n: (sequence.index(n), n), l))
        if first[0] > ind:
            first = (ind, last_n)
    wins.append((*first, board))

winning_row = min(wins)
ind, last_n, board = winning_row

marked = sequence[:ind+1]
unmarked = set([i for row in board for i in row]) - set(marked)

last_n = int(last_n)
print("winning",sum(map(int,unmarked)) * last_n)

losing_row = max(wins)
ind, last_n, board = losing_row

marked = sequence[:ind+1]
unmarked = set([i for row in board for i in row]) - set(marked)

last_n = int(last_n)
print("losing",sum(map(int,unmarked)) * last_n)
