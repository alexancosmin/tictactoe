#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 
import os
from random import randint

class bcolors:
    BLUE = '\033[1;94m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    RED = '\033[1;91m'
    DEFAULT = '\033[1;0m'

def title():
    print(bcolors.RED+"xxxxxxxxxx   xx   xxxxxxxxxx      xxxxxxxxxx   xxxxxxxxxx   xxxxxxxxxx"+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xx   xx                  xx       xx      xx   xx        "+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xx   xx                  xx       xxxxxxxxxx   xx        "+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xx   xx                  xx       xx      xx   xx        "+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xx   xxxxxxxxxx          xx       xx      xx   xxxxxxxxxx"+ bcolors.DEFAULT)
    print()
    print(bcolors.RED+"xxxxxxxxxx   xxxxxxxxxx   xxxxxxxxxx      xxxxxxxxxx     xxxxxxxxxx"+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xx      xx   xx                      xx     xx      xx"+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xx      xx   xxxxxxxxxx      xxxxxxxxxx     xx      xx"+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xx      xx   xx                      xx     xx      xx"+ bcolors.DEFAULT)
    print(bcolors.RED+"    xx       xxxxxxxxxx   xxxxxxxxxx      xxxxxxxxxx  x  xxxxxxxxxx"+ bcolors.DEFAULT)
    print()

def initGame():
    board={"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
    return board

def initHelp():
    board={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
    return board

def setPosition(player, input, board):
    board[str(input)]=player
    return board

def inputVeryfication(player, sign, board):
    playButtons = [1,2,3,4,5,6,7,8,9]
    while True:
        if player=="Computer":
            p=randint(1, 9)
        else:
            p=input(str(player) + " " + sign + ": ")
        try:
            p=int(p)
            if p in playButtons:
                if board[str(p)] == 'X' or board[str(p)] == 'O':
                    print("This field is occupied. Try again!")
                    continue
                else:
                    break
            else:
                print("Invalid field number. Enter a number between 1 and 9.")
                continue
        except:
            print("Invalid entry, try again!")
            continue
    return p

def graphics(p):
    print(bcolors.YELLOW+ "        ||        ||" + bcolors.DEFAULT)
    print(bcolors.YELLOW+ "   "+ bcolors.DEFAULT,bcolors.BLUE+ p["7"]+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ p["8"]+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ p["9"]+ bcolors.DEFAULT,)
    print(bcolors.YELLOW+ "        ||        ||" + bcolors.DEFAULT)
    print(bcolors.YELLOW+ "==============================" + bcolors.DEFAULT)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "   "+ bcolors.DEFAULT,bcolors.BLUE+ p["4"]+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ p["5"]+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ p["6"]+ bcolors.DEFAULT,)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "=============================="+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "   "+ bcolors.DEFAULT,bcolors.BLUE+ p["1"]+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ p["2"]+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ p["3"]+ bcolors.DEFAULT,)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)

def addToScoreTable(player, scoreTable):
    if player in scoreTable:
        scoreTable[player] += 1
    else:
        scoreTable[player]= 1

def presentScoreTable(scoreTable):
    for item in scoreTable:
        print(bcolors.BLUE+"||  "+ str(scoreTable[item])+"  points for  " +item+ bcolors.BLUE)

def check(p,P,sign,scoreTable):
    if ((p["1"]==sign and p["2"]==sign and p["3"]==sign)
        or(p["4"]==sign and p["5"]==sign and p["6"]==sign)
        or(p["7"]==sign and p["8"]==sign and p["9"]==sign)
        or(p["1"]==sign and p["4"]==sign and p["7"]==sign)
        or(p["2"]==sign and p["5"]==sign and p["8"]==sign)
        or(p["3"]==sign and p["6"]==sign and p["9"]==sign)
        or(p["1"]==sign and p["5"]==sign and p["9"]==sign)
        or(p["3"]==sign and p["5"]==sign and p["7"]==sign)):
        print(bcolors.RED+P+" " +"\""+ sign + "\" WINS!"+bcolors.DEFAULT)
        addToScoreTable(P,scoreTable)
        presentScoreTable(scoreTable)
        return False
    elif ' ' not in p.values():
        print(bcolors.RED+"DRAW"+bcolors.DEFAULT)
        presentScoreTable(scoreTable)
        return False
    return True

def game(player1,player2,scoreTable):
    p=initGame()
    os.system('clear')
    graphics(p)
    flag=True
    while True:
        p1 = inputVeryfication(player1,"X",p)
        setPosition("X",p1,p)
        os.system('clear')
        graphics(p)
        flag = check(p,player1,"X",scoreTable)
        if not flag:
            break
        flag = check(p,player2,"O",scoreTable)
        if not flag:
            break
        p2 = inputVeryfication(player2, "O",p)
        setPosition("O",p2,p)
        os.system('clear')
        graphics(p)
        flag=check(p,player1,"X",scoreTable)
        if not flag:
            break
        flag = check(p,player2,"O",scoreTable)
        if not flag:
            break

def helpMenuInfo():
    os.system('clear')
    p=initHelp()
    graphics(p)
    print()

def helpMenuRules():
    os.system('clear')
    print(bcolors.GREEN+ "Each player takes a turn and selects a field \nwhich they wish to place their marker on by\ntyping a corresponding number. \nThe goal of the game is to place 3 of your markers \nin a straight line (vertical, horizontal or diagonal)." + bcolors.DEFAULT)
    print()

def helpMenu(scoreTable):
    os.system('clear')
    help_select = input(bcolors.GREEN+ "Type:\n\'r\' for rules\n\'i\' for key input\n\'q\' for back to main menu\n:" + bcolors.DEFAULT)
    if help_select == "i":
        helpMenuInfo()
    elif help_select == "r":   
        helpMenuRules()
    elif help_select == "q":   
        mainMenu(scoreTable)
    else:
        invaliEntry()
        helpMenu(scoreTable)

def getPlayerName(player):
    return input(bcolors.GREEN+ "Enter name for "+ player + ":\n" + bcolors.DEFAULT)

def gameMenu(scoreTable):
    game_type = input(bcolors.GREEN+ "Type:\n\'1\' for single player \n\'2\' for multiplayer\n:" + bcolors.DEFAULT)
    if game_type == "1":
        P1=getPlayerName("Player One")
        P2=bcolors.GREEN+ "Computer" + bcolors.DEFAULT
        game(P1,"Computer",scoreTable)
    elif game_type == "2":
        P1=getPlayerName("Player One")
        P2=getPlayerName("Player Two")
        game(P1,P2,scoreTable)
    else:
        print(bcolors.RED+"Invalid entry, try again."+ bcolors.DEFAULT)
        gameMenu(scoreTable)

def invaliEntry():
    print(bcolors.RED+"Invalid entry, try again."+ bcolors.DEFAULT)

def mainMenu(scoreTable):
    menu_select = input(bcolors.GREEN+ " Type \'s\' to start new game \n Type \'h\' for help \n Type \'q\' to quit \n:" + bcolors.DEFAULT) 
    if menu_select == "s":
        os.system('clear')
        gameMenu(scoreTable)
        mainMenu(scoreTable)
    elif menu_select == "h":
        os.system('clear')
        helpMenu(scoreTable)
        mainMenu(scoreTable)
    elif menu_select == "q":
        exit(0)
    else:
        invaliEntry()
        mainMenu(scoreTable)

def main():
    os.system('clear')
    title()
    scoreTable={}
    mainMenu(scoreTable)

main()