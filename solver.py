def show_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and not (i == 0):
            print("- - - - - - - - - - - - ")
        
        for j in range(len(brd)):
            if j % 3 == 0 and not (j == 0):
                print(" | ", end="") #end does not make it go to new line

            if j == 8:
                    print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")

# Begins top left and goes down right
def findEmptySqaure(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row,col)
    return None

def solve(brd):
    
    find = findEmptySqaure(brd)

    # If there are no empty squres, solution found
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(brd, i, (row,col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False    



def valid(brd, entry, pos):

    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == entry and pos[1] != i:
            return False
    

    #Check col
    for j in range(len(brd)):
        if brd[i][pos[1]] == entry and pos[0] != j:
            return False
    
    #Check 3x3 square
    #Need to determine which box we are in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y *3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if brd[i][j] == entry and (i,j) != pos:
                return False
    
    return True


