#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 
import os

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'

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

def setPosition(player, input, board):
    board[str(input)]=player
    return board

def inputVeryfication(player, sign, board):
    playButtons = [1,2,3,4,5,6,7,8,9]
    while True:
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

def showResult():
    print(bcolors.RED+P+" " + sign + " WIN!"+bcolors.DEFAULT)

def check(p,P,sign):
    if ((p["1"]==sign and p["2"]==sign and p["3"]==sign)
        or(p["4"]==sign and p["5"]==sign and p["6"]==sign)
        or(p["7"]==sign and p["8"]==sign and p["9"]==sign)
        or(p["1"]==sign and p["4"]==sign and p["7"]==sign)
        or(p["2"]==sign and p["5"]==sign and p["8"]==sign)
        or(p["3"]==sign and p["6"]==sign and p["9"]==sign)
        or(p["1"]==sign and p["5"]==sign and p["9"]==sign)
        or(p["3"]==sign and p["5"]==sign and p["7"]==sign)):
        print(bcolors.RED+P+" " + sign + " WIN!"+bcolors.DEFAULT)
        return False
    elif ' ' not in p.values():
        print(bcolors.RED+"DRAW"+bcolors.DEFAULT)
        return False
    return True

def gameSingle():
    print("Single")

def gameMultiplayer(player1,player2):
    p=initGame()
    os.system('clear')
    graphics(p)
    flag=True
    while True:
        p1 = inputVeryfication(player1,"X",p)
        setPosition("X",p1,p)
        os.system('clear')
        graphics(p)
        flag = check(p,player1,"X")
        if not flag:
            break
        flag = check(p,player2,"O")
        if not flag:
            break
        p2 = inputVeryfication(player2, "O",p)
        setPosition("O",p2,p)
        os.system('clear')
        graphics(p)
        flag=check(p,player1,"X")
        if not flag:
            break
        flag = check(p,player2,"O")
        if not flag:
            break

def help():
    os.system('clear')
    print("\n")
    print(bcolors.GREEN+" Key input:"+ bcolors.DEFAULT)
    print("\n")
    print(bcolors.YELLOW+ "        ||        ||" + bcolors.DEFAULT)
    print(bcolors.YELLOW+ "   "+ bcolors.DEFAULT,bcolors.BLUE+ "7" + bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ "8" + bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ "9" + bcolors.DEFAULT,)
    print(bcolors.YELLOW+ "        ||        ||" + bcolors.DEFAULT)
    print(bcolors.YELLOW+ "==============================" + bcolors.DEFAULT)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "   "+ bcolors.DEFAULT,bcolors.BLUE+ "4"+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ "5"+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ "6" + bcolors.DEFAULT,)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "=============================="+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)
    print(bcolors.YELLOW+ "   "+ bcolors.DEFAULT,bcolors.BLUE+ "1"+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ "2"+ bcolors.DEFAULT,bcolors.YELLOW+"  ||   "+ bcolors.DEFAULT,bcolors.BLUE+ "3"+ bcolors.DEFAULT,)
    print(bcolors.YELLOW+ "        ||        ||"+ bcolors.DEFAULT)
    print("\n")
          
def helpMenuInfo():
    help()

def helpMenuRules():
    print(bcolors.GREEN+ "Each player takes a turn and selects a field \nwhich they wish to place their marker on by \ntyping a corresponding number. \nThe goal of the game is to place 3 of your markers \nin a straight line (vertical, horizontal or diagonal)." + bcolors.DEFAULT)

def helpMenu():
    os.system('clear')
    help_select = input(bcolors.GREEN+ "Type \'r\' for rules or \'i\' for key input \n :" + bcolors.DEFAULT)
    if help_select == "i":
        os.system('clear')
        helpMenuInfo()
    elif help_select == "r":
        os.system('clear')
        helpMenuRules()
    else:
        invaliEntry()
        helpMenu()        

def gameMenu():
    game_type = input(bcolors.GREEN+ "Type \'1\' for single player or \'2\' for multiplayer \n :" + bcolors.DEFAULT)
    if game_type == "1":
        P1=input(bcolors.GREEN+ "Enter name for Player One \n :" + bcolors.DEFAULT)
        gameSingle()
    elif game_type == "2":
        P1=input(bcolors.GREEN+ "Enter name for Player One \n :" + bcolors.DEFAULT)
        P2=input(bcolors.GREEN+ "Enter name for Player Two \n :" + bcolors.DEFAULT)
        gameMultiplayer(P1,P2)
    else:
        print(bcolors.RED+"Invalid entry, try again."+ bcolors.DEFAULT)
        gameMenu()

def invaliEntry():
    print(bcolors.RED+"Invalid entry, try again."+ bcolors.DEFAULT)

def mainMenu():
    menu_select = input(bcolors.GREEN+ " Type \'s\' to start new game \n Type \'h\' for help \n Type \'q\' to quit \n:" + bcolors.DEFAULT) 
    if menu_select == "s":
        os.system('clear')
        gameMenu()
        mainMenu()
    elif menu_select == "h":
        os.system('clear')
        helpMenu()
        mainMenu()
    elif menu_select == "q":
        exit(0)
    else:
        invaliEntry()
        mainMenu()

def main():
    os.system('clear')
    title()
    mainMenu()

main()