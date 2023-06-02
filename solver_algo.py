def print_board(board):
    '''To print the Input and Output Board.'''

    sub_board_len = int(len(board)**0.5)

    for i in range(len(board)):
        if i % sub_board_len == 0 and i != 0:
            print('- '* sub_board_len * 4)
        
        for j in range(len(board[0])):
            if j % sub_board_len == 0 and j != 0:
                print(' | ', end='')

            if j == len(board) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

def find_empty(board):
    '''Checking and returning empty grid coordinates.'''

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col
    return None

def isValid(board, num, pos):
    '''Validating a particular number on a particular position 
                of the preset board pattern.'''
    # To check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # To check column
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check each box
    sub_board_len = int(len(board)**0.5)
    box_x = pos[1] // sub_board_len 
    box_y = pos[0] // sub_board_len

    for i in range(box_y * sub_board_len, box_y * sub_board_len + sub_board_len):
        for j in range(box_x * sub_board_len, box_x * sub_board_len + sub_board_len):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    '''Backtracking Algorithm for solving the board.'''

    find = find_empty(board)
    if not find:
        return True
    row, col = find
    
    for num in range(1, len(board)+1):
        if isValid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


if __name__ == '__main__':
    myBoard =[  
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
       ] 

    print_board(myBoard)
    solve(myBoard)
    print('=======================')
    print_board(myBoard)
