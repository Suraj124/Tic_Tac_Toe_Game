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

the_board=['','1','2','3','4','5','6','7','8','9']
place_marker(the_board,'@',5)
display_board(the_board)

