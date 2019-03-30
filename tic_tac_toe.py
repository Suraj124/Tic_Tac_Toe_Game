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
        return 'player2'
    else:
        return 'player1'

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
    return input("Do you want to play Agian? y or n : ").lower().startswith('y')


while True:
    the_board=[' ']*10
    player1_mark,player2_mark=player_input()

    turn=check_first()
    print(turn,"will play first")

    play_game=input("Ready to play? y or no : ").lower().startswith('y')
    
    if play_game:
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn == "player1":

            display_board(the_board)
            print('Player 1 ')
            position=player_position(the_board)
            place_marker(the_board,player1_mark,position)
            if check_win(the_board,player1_mark):
                display_board(the_board)
                print('Player 1 Has Won')
                game_on=False
            else:
                if check_tie(the_board):
                    display_board(the_board)
                    print("GAME TIE")
                else:
                    turn='player2'
        else:
            display_board(the_board)
            print('Player 2 ')
            position=player_position(the_board)
            place_marker(the_board,player2_mark,position)
            if check_win(the_board,player2_mark):
                display_board(the_board)
                print('Player 2 Has Won')
                game_on=False
            else:
                if check_tie(the_board):
                    display_board(the_board)
                    print("GAME TIE")
                else:
                    turn='player1'
    if not replay():
        break


    

