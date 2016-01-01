#! python3

import random

#initialize the board
Board = {'tl':1,'tm':0,'tr':' ','ml':' ','mm':' ','mr':' ','ll':' ','lm':' ','lr':' '}

def printBoard(myBoard):
#display the board
    print ('Current board is:: ')
    print (myBoard['tl']+ '|'+ myBoard['tm'] +'|'+myBoard['tr'])
    print ('-+-+-')
    print (myBoard['ml']+ '|'+ myBoard['mm'] +'|'+myBoard['mr'])
    print ('-+-+-')
    print (myBoard['ll']+ '|'+ myBoard['lm'] +'|'+myBoard['lr'])

#translation logic for display of 'O' and 'X'
def prettyBoard(myBoard):
    prettyB = {'tl':' ','tm':' ','tr':' ','ml':' ','mm':' ','mr':' ','ll':' ','lm':' ','lr':' '}
    for board_loc, character in myBoard.items():
        if character == 1:
            prettyB[board_loc] = 'O'
        elif character == 0:
            prettyB[board_loc] = 'X'
        else:
            prettyB[board_loc] = ' '
    return prettyB

#cointoss logic to determine who goes first
cointoss = random.randint(0,1)
if cointoss == 0:
    print ('I go first')
else:
    print('You go first')

#Check logic
def checkBoard(myBoard):
    winner = ' '
    #check for 'O' or 'X' in horizontal rows
    if (myBoard['tl'] ^  myBoard['tm']) ^ myBoard['tr'] == 0:
        winner = myBoard['tl']
    if (myBoard['ml'] ^ myBoard['mm']) ^ myBoard['mr'] == 0:
        winner = myBoard['ml']
    if (myBoard['ll'] ^ myBoard['lm']) ^ myBoard['lr'] == 0:
        winner = myBoard['ll']
    #check for 'O' or 'X' in vertical rows
    if (myBoard['tl'] ^ myBoard['ml']) ^ myBoard['ll'] == 0:
        winner = myBoard['tl']
    if (myBoard['tm'] ^ myBoard['mm']) ^ myBoard['lm'] == 0:
        winner = myBoard['mm']
    if (myBoard['tr'] ^ myBoard['mr']) ^ myBoard['lr'] == 0:
        winner = myBoard['lr']
    #check for 'O' or 'X' in diagonal-1
    if (myBoard['tl'] ^ myBoard['mm']) ^ myBoard['lr'] == 0:
        winner = myBoard['t1']
    #check for 'O' or 'X' in diagonal-2
    if (myBoard['tr']^ myBoard['mm']) ^ myBoard['ll'] == 0:
        winner = myBoard['tr']
    return winner


for turn in range(0,7):
    print("The current board is:\n")
    printBoard(prettyBoard(Board))
    print("Where should I mark the piece?")
    mark = input()
    if mark == 'tl' or mark == 'tm' or mark == 'tr' or mark == 'mr' or mark == 'mm' or mark == 'ml' or mark == 'll' or mark == 'lm' or mark == 'lr':
        Board[mark]=1
    else:
        print("Incorrect Spatial Position... Try Again")
        turn = turn - 1
    #winner declaration
    winner = checkBoard(Board)
    if winner != ' ':
        print ('Winner is: '+ winner)
        break;
print("Thank you for playing!")

