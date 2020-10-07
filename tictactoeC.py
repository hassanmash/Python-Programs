import copy

theBoard = {
    "TL":" ","TM":" ","TR":" ",
    "ML":" ","MM":" ","MR":" ",
    "BL":" ","BM":" ","BR":" ",
}

def printBoard(board):
    print(board['TL'],'|',board['TM'],'|',board['TR'],sep="")
    print("-+-+-")
    print(board['ML'],'|',board['MM'],'|',board['MR'],sep="")
    print("-+-+-")
    print(board['BL'],'|',board['BM'],'|',board['BR'],sep="")
    print("-+-+-")
def clearBoard(board):
    board['TL'] = " "
    board['TM'] = " "
    board['TR'] = " "
    board['ML'] = " "
    board['MM'] = " "
    board['MR'] = " "
    board['BL'] = " "
    board['BM'] = " "
    board['BR'] = " "
def ifdraw(board):
    if board['TL'] == " ":
        return False
    elif board['TM'] == " ":
        return False
    elif board['TR'] == " ":
        return False
    elif board['ML'] == " ":
        return False
    elif board['MM'] == " ":
        return False
    elif board['MR'] == " ":
        return False
    elif board['BL'] == " ":
        return False
    elif board['BM'] == " ":
        return False
    elif board['BR'] == " ":
        return False
    else:
        return True
def checkwinner(board):
    if (board['TL'] =='X' and board['TM'] =='X' and board['TR'] == 'X'):
        w = "X"
        return w
    elif(board['TL'] =='O' and board['TM'] =='O' and board['TR'] == 'O'):
        w = "O"
        return w
    elif (board['ML'] =='X' and board['MM'] =='X' and board['MR'] == 'X'):
        w = "X"
        return w
    elif(board['ML'] =='O' and board['MM'] =='O' and board['MR'] == 'O'):
        w = "O"
        return w
    elif (board['BL'] =='X' and board['BM'] =='X' and board['BR'] == 'X'):
        w = "X"
        return w
    elif(board['BL'] =='O' and board['BM'] =='O' and board['BR'] == 'O'):
        w = "O"
        return w
    elif (board['TL'] =='X' and board['MM'] =='X' and board['BR'] == 'X'):
        w = "X"
        return w
    elif(board['TL'] =='O' and board['MM'] =='O' and board['BR'] == 'O'):
        w = "O"
        return w
    elif (board['TR'] =='X' and board['MM'] =='X' and board['BL'] == 'X'):
        w = "X"
        return w
    elif(board['TR'] =='O' and board['MM'] =='O' and board['BL'] == 'O'):
        w = "O"
        return w
    elif (board['TL'] =='X' and board['ML'] =='X' and board['BL'] == 'X'):
        w = "X"
        return w
    elif(board['TL'] =='O' and board['ML'] =='O' and board['BL'] == 'O'):
        w = "O"
        return w
    elif (board['TM'] =='X' and board['MM'] =='X' and board['BM'] == 'X'):
        w = "X"
        return w
    elif(board['TM'] =='O' and board['MM'] =='O' and board['BM'] == 'O'):
        w = "O"
        return w
    elif (board['TR'] =='X' and board['MM'] =='X' and board['BL'] == 'X'):
        w = "X"
        return w
    elif(board['TR'] =='O' and board['MR'] =='O' and board['BR'] == 'O'):
        w = "O"
        return w
    else:
        w = "IC"
        return w
def placeinboard(pos):
    if (pos == "TL" or pos == "TM" or pos == "TR" or pos == "ML" or pos == "MM" or pos == "MR" or pos == "BL" or pos == "BM" or pos == "BR"):
        if(theBoard[pos]=="X" or theBoard[pos]=="O"):
            print("This position is already filled by",theBoard[pos])
        else:
            if(turn == plyr1):
                theBoard[pos] = plyr1
            else:
                theBoard[pos] = plyr2
    else:
        print("Please enter correct position!")

print("---------Let's Enjoy the game!---------")
plyr1 = None
plyr2 = None
while True:
    plyr1 = input("Enter the letter for player 1: (X/O)")
    if (plyr1 == "X"):
        plyr1 = "X"
        plyr2 = "O"
        break
    elif (plyr1 == "x"):
        plyr1 = "X"
        plyr2 = "O"
        break
    elif (plyr1 == "O"):
        plyr1 = "O"
        plyr2 = "X"
        break
    elif (plyr1 == "o"):
        plyr1 = "O"
        plyr2 = "X"
        break
    else:
        print("Please enter a valid letter(Refer brackets for no errors!)")
turn = plyr1
p1score = 0
p2score = 0
while True:
    print("Player 1 score:",p1score,"                Player 2 score:",p2score)
    print("Do you want to continue?")
    cont = input("y/n : ")
    if (cont == "n" or cont == "N"):
        break
    else:
        while True:
            printBoard(theBoard)
            print('Turn for',turn,'- enter the position:',end=" ")
            x = input()
            temp = copy.copy(theBoard)
            placeinboard(x)
            if(temp==theBoard):
                continue
            if turn == plyr1:
                turn = plyr2
            else:
                turn = plyr1
            win = checkwinner(theBoard)
            y = ifdraw(theBoard)
            if y:
                break
            if win == plyr1:
                print("Player",plyr1,"wins!")
                printBoard(theBoard)
                p1score +=1
                clearBoard(theBoard)
                break
            elif win == plyr2:
                print("Player",plyr2,"wins!")
                printBoard(theBoard)
                p2score += 1
                clearBoard(theBoard)
                break
            else:
                continue
        draw = checkwinner(theBoard)
        if draw == "IC":
            print("Draw!")
            printBoard(theBoard)
            clearBoard(theBoard)
if(p1score > p2score):
    print("Player 1 ( with letter",plyr1,") Won the game with",p1score,"points!")
elif (p2score > p1score):
    print("Player 2 ( with letter",plyr2,") Won the game with",p2score,"points!")
else:
    print("Its a DRAW!. Congratulations both of you!")