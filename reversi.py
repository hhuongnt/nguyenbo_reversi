import string
a = string.ascii_lowercase


def create_board():
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'W', 'B', '.', '.', '.'],
             ['.', '.', '.', 'B', 'W', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]
    anp = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in anp:
        print(i, end=' ')
    print('')
    num = 1
    for i in board:
        print(num, end=' ')
        num += 1
        for j in i:
            print(j, end=' ')
        print('')
    return board
# =====================================================


def nextcell(x, y):
    directs = [[-1, 0], [-1, 1], [0, 1], [1, 1],    # directions of cell
               [1, 0], [1, -1], [0, -1], [-1, -1]]
    next = []                                 # list chua toa do next_cell
    for dx, dy in directs:
        pair_next = (x + dx, y + dy)
        next.append([pair_next, dx, dy])
    return next                       # phai cong voi directs de di tiep duong

# =====================================================


def check(board, next, color):            # lay huong di duoc trong directs
    allow = []
    for n1, dx, dy in next:
        if board[n1[0]][n1[1]] == color or board[n1[0]][n1[1]] == ".":
            pass
        else:
            n = [n1[0] + dx, n1[1] + dy]
            allow.append(n)
    return allow
# ==========================================================


def valid_moves(board, color):
    cell = []               # toa do cua color
    allow = []
    valid = []
    all = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            next = []
            if(board[i][j] != color):
                pass
            else:
                next = nextcell(i, j)       # toa do cac direcions
                allow += check(board, next, color)
    for x, y in allow:
        y = (y+1)
        x = a[x]
        c = [x, str(y)]
        all.append(c)
    print("Valid choices: ", end='')
    for x, y in all:
        print(x + y, end=' ')
    print('')


return all

# valid_moves(create_board(), "B")


def update_board(valid, board, color):
    index = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    board[[index[valid[0]]int(valid[1])]] = color
    directs = [[-1, 0], [-1, 1], [0, 1], [1, 1],    # directions of cell
               [1, 0], [1, -1], [0, -1], [-1, -1]]
    outer = ['1', '2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', '', '.', ' ']
    for dir_row, dir_col in directs:
        col = index[valid[0]]
        row = int(valid[1])
        replace = []
        if row in range(1, 9) and col in range(1, 9):
            while (board[row + dir_row][col + dir_col] != color
                    and board[row + dir_row][col + dir_col] not in outer):
                row += dir_row
                col += dir_col
                replace.append((row, col))
            if board[row + dir_row][col + dir_col] in outer:
                replace = []
        if replace != []:
            for r1, r2 in replace:
                board[r1][r2] = color
    return board


def result(board):
    count_b = 0
    count_w = 0
    for row in board:
        for i in row:
            if i == 'B':
                count_b += 1
            if i == 'W':
                count_b += 1
    print('W: ', count_b, ', B: ', count_w)
    if count_b > count_w:
        print('B wins.')
    elif count_w > count_b:
        print('W wins.')
    else:
        print("Draw")


board = create_board()
valid_moves(board, "B")
input('Player B:', end='')
update_board(valid_moves(create_board(), "B"), create_board(), 'B')
valid_moves(update_board(valid_moves(create_board(), "B"),
            create_board(), 'B'), "W")
while True:
    input('Player B:', end='')
    update_board(valid_moves(),)
    valid_moves(update_board(valid_moves(create_board(), "B"),
                create_board(), 'B'), "W")

# turn = 'B'
# end_black = 1
# end_white = 1
# while end_black != -1 or end_white != -1:
#     if turn > 0:
#         if b_choice(mainBoard) != set():
#             print("Valid choices:", *b_choice(mainBoard))
#             choice = input('Player B: ')
#             while choice not in b_choice(mainBoard):
#                 print('Invalid choice')
#                 choice = input('Player B: ')
#             mainBoard = update_board(choice, mainBoard, 'B')
#             drawBoard(mainBoard)
#             end_black = 1
#         else:
#             end_black = -1
#             if end_black == end_white:
#                 print('Player B cannot play')
#                 print("End of the game. ", end='')
#             else:
#                 print('Player B cannot play')
#                 drawBoard(mainBoard)
#         turn = turn * -1
#     else:
#         if w_choice(mainBoard) != set():
#             print("Valid choices:", *w_choice(mainBoard))
#             choice = input('Player W: ')
#             while choice not in w_choice(mainBoard):
#                 print('Invalid choice')
#                 choice = input('Player W: ')
#             mainBoard = update_board(choice, mainBoard, 'W')
#             drawBoard(mainBoard)
#             end_white = 1
#         else:
#             end_white = -1
#             if end_black == end_white:
#                 print('Player W cannot play')
#                 print("End of the game. ", end='')
#             else:
#                 print('Player W cannot play')
#                 drawBoard(mainBoard)
#         turn = turn * -1
# result(mainBoard)
