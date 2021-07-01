board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def show_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and not (i == 0):
            print("- - - - - - - - - - - - ")
        
        for j in range(len(brd)):
            if j % 3 == 0 and not j == 0:
                print(" | ", end="") #end does not make it go to new line

            if j == 8:
                    print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")



