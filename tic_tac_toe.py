from random import randint
def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')

def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input("Player 1, Choose X or O : ")
    player1=marker

    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)

def place_marker(board,mark,position):
    board[position]=mark

def check_win(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or 
    (board[5]==mark and board[6]==mark and board[7]==mark) or 
    (board[1]==mark and board[2]==mark and board[3]==mark) or 
    (board[1]==mark and board[4]==mark and board[7]==mark) or 
    (board[2]==mark and board[5]==mark and board[8]==mark) or 
    (board[3]==mark and board[6]==mark and board[9]==mark) or 
    (board[1]==mark and board[5]==mark and board[9]==mark) or 
    (board[3]==mark and board[5]==mark and board[7]==mark))

def check_first():
    if randint(0,1)==0:
        return 'Player2'
    else:
        return 'Player1'

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

def replay():
    return input("Do you want to play Agian? y or n").lower().startswith('y')



