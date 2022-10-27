# SudoKosolover
# sudoko board
board = [
    [4,0,0,0,0,0,0,0,0],
    [1,0,0,5,0,9,7,3,0],
    [0,0,0,0,4,0,0,1,9],
    [2,0,4,6,0,8,1,9,7],
    [0,0,0,0,5,1,0,0,2],
    [0,0,3,4,0,2,0,0,8],
    [3,0,5,8,0,0,9,2,6],
    [7,0,6,0,0,0,8,5,0],
    [8,0,1,0,0,5,4,7,0],
]


# printing table like board
def print_board(board):
    for sublist in range(len(board)):
        print("\n", end='')
        if sublist%3==0 and sublist!=0:
            print("-"*22, end="\n")
        for num in range(len(board[sublist])):
            if num%3==0 and num!=0:
                print("| ", end='')
            print(board[sublist][num], end=' ')
    print()



# Finding empty places and puttin them into a list named blank_pos
def empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)
    return None,None


# checking the number is valid for the place or not
def valid(board, guess, row,col):
    row_val= board[row]

    if guess in row_val:
        return False

    col_val = [board[i][col] for i in range(9)]
    if guess in col_val:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start+3):
            if board[r][c] == guess:
                return False
    return True

# solving board 
def solve(board):
    row,col=empty(board)

    if row is None:
        return True

    for guess in range(1,10):
        if valid(board, guess, row, col):
            board[row][col] = guess
            if solve(board):
                return True
        board[row][col] = 0
        
    return False


# calling function
print("     Soduko  Table  ")
print_board(board)
solve(board)
print("       Solved   ")
print_board(board)