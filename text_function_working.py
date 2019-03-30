def space_check(board,position):
    return board[position]==' '

def player_position(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Enter your position (1-9): "))
    return position

def check_tie(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True