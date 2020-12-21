import sys

input = [[*line.strip()] for line in sys.stdin]

def flatstring(board):
    return ''.join([e for row in board for e in row])

def match(board1, board2):
    return flatstring(board1) == flatstring(board2)

# -----------------------------------------------------------------------------
# part 1: 2303

def countadjacentoccupied(board, row, col):
    # brutal force
    count = 0
    for r in range(row-1, row+2):
        if r >= 0 and r < len(board):
            for c in range(col-1, col+2):
                if c >= 0 and c < len(board[r]):
                    if (r != row or c != col) and board[r][c] == '#':
                        count += 1
    return count

def gen1(board):
    next = [['.']*len(row) for row in board]
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] != '.':
                count = countadjacentoccupied(board, row, col)
                if board[row][col] == 'L' and count == 0:
                    next[row][col] = '#'
                elif board[row][col] == '#' and count >= 4:
                    next[row][col] = 'L'
                else:
                    next[row][col] = board[row][col]
    return next


# run gen1 until stabilized
board = input
nextboard = gen1(board)
while not match(board, nextboard):
    board = nextboard
    nextboard = gen1(board)

print(f"part 1: {flatstring(board).count('#')}")

# -----------------------------------------------------------------------------
# part 2: 2057

# in:  list of lists of [., L, #]
# out: list of lists of visible occupied seats from each position in the list
# considers one list at a time
def build_list_counts(lists):
    counts = []
    for l in lists:
        left = False
        right = False
        nums = [0] * len(l)
        counts.append(nums)
        for index in range(len(l)):
            # go forward and backward through the list
            # to determine visibility to the left and right of each spot
            if l[index] != '.':
                if left: nums[index] += 1
                left = l[index] == '#'
            rightindex = len(l)- index - 1
            if l[rightindex] != '.':
                if right: nums[rightindex] += 1
                right = l[rightindex] == '#'
    return counts

# in:  list of lists of [., L, #]
# out: list of lists of visible occupied seats from each position in the board
# considers the entire board
def build_count_matrix(board):
    # decompose to rows, cols, fdiags (from top left), bdiags (from bottom left)
    # https://stackoverflow.com/a/43311126/1630953
    max_row = len(board)
    max_col = len(board[0])
    rows = [[] for _ in range(max_row)]
    cols = [[] for _ in range(max_col)]
    fdiags = [[] for _ in range(max_row + max_col - 1)]
    bdiags = [[] for _ in range(len(fdiags))]
    min_bdiag = -max_row + 1

    for c in range(max_col):
        for r in range(max_row):
            rows[r].append(board[r][c])
            cols[c].append(board[r][c])
            fdiags[c+r].append(board[r][c])
            bdiags[c-r-min_bdiag].append(board[r][c])

    # for each of those, get forward and backward counts
    row_vis_counts = build_list_counts(rows)
    col_vis_counts = build_list_counts(cols)
    fdiag_vis_counts = build_list_counts(fdiags)
    bdiag_vis_counts = build_list_counts(bdiags)

    # recompose to matrix of numbers
    count_matrix = [[0]*len(row) for row in board]
    for c in range(max_col):
        for r in range(max_row):
            # rows
            count_matrix[r][c] += row_vis_counts[r][c]

            # cols
            count_matrix[r][c] += col_vis_counts[c][r]

            dnum = r+c
            i = c - max(r + c - len(board) + 1, 0)
            # print(f'{r},{c} - {board[r][c]} - fdiag#: {dnum} - i: {i}')
            count_matrix[r][c] += fdiag_vis_counts[r+c][i]

            dnum = c-r-min_bdiag
            i = c - max(dnum - len(board) + 1, 0)
            # print(f'{r},{c} - {board[r][c]} - bdiag#: {dnum} - i: {i}')
            count_matrix[r][c] += bdiag_vis_counts[dnum][i]
    return count_matrix

def gen2(board):
    # get visibility numbers for each seat on the board
    count_matrix = build_count_matrix(board)

    # apply visibility numbers to board to get next generation
    # (so similar to gen1 - if doing it again I'd consolidate gen1 and gen2
    #  which would also make gen1 more efficient)
    next = [['.']*len(row) for row in board]
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] != '.':
                count = count_matrix[row][col]
                if board[row][col] == 'L' and count == 0:
                    next[row][col] = '#'
                elif board[row][col] == '#' and count >= 5:
                    next[row][col] = 'L'
                else:
                    next[row][col] = board[row][col]
    return next

# run gen2 until stabilized
board = input
nextboard = gen2(board)
while not match(board, nextboard):
    board = nextboard
    nextboard = gen2(board)

print(f"part 2: {flatstring(board).count('#')}")
