sequence = []
boards = []

# Parse input data
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

# For every board, find out when it wins
wins = []
for board in boards:
    rc = board + [*zip(*board[::-1])]
    first = len(sequence),
    for l in rc:
        ind, last_n = max(map(lambda n: (sequence.index(n), n), l))
        if first[0] > ind:
            first = (ind, last_n)
    wins.append((*first, board))

# Calculate the score of a given board and its winning number
def score(ind, last_n, board):
    marked = sequence[:ind+1]
    unmarked = set([i for row in board for i in row]) - set(marked)
    last_n = int(last_n)

    return sum(map(int,unmarked)) * last_n

# Output best and worst boards
winning_board = min(wins)
losing_board = max(wins)

print("winning",score(*winning_board))
print("losing",score(*losing_board))
