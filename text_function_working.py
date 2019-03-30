from random import randint
def check_first():
    if randint(0,1)==0:
        return 'Player2'
    else:
        return 'Player1'
print(check_first())
