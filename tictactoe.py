#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def title():
    print(bcolors.FAIL+"xxxxxxxxxx   xx   xxxxxxxxxx      xxxxxxxxxx   xxxxxxxxxx   xxxxxxxxxx"+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xx   xx                  xx       xx      xx   xx        "+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xx   xx                  xx       xxxxxxxxxx   xx        "+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xx   xx                  xx       xx      xx   xx        "+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xx   xxxxxxxxxx          xx       xx      xx   xxxxxxxxxx"+ bcolors.ENDC)
    print()
    print(bcolors.FAIL+"xxxxxxxxxx   xxxxxxxxxx   xxxxxxxxxx      xxxxxxxxxx     xxxxxxxxxx"+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xx      xx   xx                      xx     xx      xx"+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xx      xx   xxxxxxxxxx      xxxxxxxxxx     xx      xx"+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xx      xx   xx                      xx     xx      xx"+ bcolors.ENDC)
    print(bcolors.FAIL+"    xx       xxxxxxxxxx   xxxxxxxxxx      xxxxxxxxxx  x  xxxxxxxxxx"+ bcolors.ENDC)
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
    os.system('clear')
    print(bcolors.WARNING+ "        ||        ||" + bcolors.ENDC)
    print(bcolors.WARNING+ "   "+ bcolors.ENDC,bcolors.OKBLUE+ p["7"]+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ p["8"]+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ p["9"]+ bcolors.ENDC,)
    print(bcolors.WARNING+ "        ||        ||" + bcolors.ENDC)
    print(bcolors.WARNING+ "==============================" + bcolors.ENDC)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)
    print(bcolors.WARNING+ "   "+ bcolors.ENDC,bcolors.OKBLUE+ p["4"]+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ p["5"]+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ p["6"]+ bcolors.ENDC,)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)
    print(bcolors.WARNING+ "=============================="+ bcolors.ENDC)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)
    print(bcolors.WARNING+ "   "+ bcolors.ENDC,bcolors.OKBLUE+ p["1"]+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ p["2"]+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ p["3"]+ bcolors.ENDC,)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)

def check(p,P,sign):
    if ((p["1"]==sign and p["2"]==sign and p["3"]==sign)
        or(p["4"]==sign and p["5"]==sign and p["6"]==sign)
        or(p["7"]==sign and p["8"]==sign and p["9"]==sign)
        or(p["1"]==sign and p["4"]==sign and p["7"]==sign)
        or(p["2"]==sign and p["5"]==sign and p["8"]==sign)
        or(p["3"]==sign and p["6"]==sign and p["9"]==sign)
        or(p["1"]==sign and p["5"]==sign and p["9"]==sign)
        or(p["3"]==sign and p["5"]==sign and p["7"]==sign)):
        print(bcolors.FAIL+P+" " + sign + " WIN!"+bcolors.ENDC)
        return False
    return True

def help():
    print("\n")
    print(bcolors.OKGREEN+" Key input:"+ bcolors.ENDC)
    print("\n")
    print(bcolors.WARNING+ "        ||        ||" + bcolors.ENDC)
    print(bcolors.WARNING+ "   "+ bcolors.ENDC,bcolors.OKBLUE+ "7" + bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ "8" + bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ "9" + bcolors.ENDC,)
    print(bcolors.WARNING+ "        ||        ||" + bcolors.ENDC)
    print(bcolors.WARNING+ "==============================" + bcolors.ENDC)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)
    print(bcolors.WARNING+ "   "+ bcolors.ENDC,bcolors.OKBLUE+ "4"+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ "5"+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ "6" + bcolors.ENDC,)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)
    print(bcolors.WARNING+ "=============================="+ bcolors.ENDC)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)
    print(bcolors.WARNING+ "   "+ bcolors.ENDC,bcolors.OKBLUE+ "1"+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ "2"+ bcolors.ENDC,bcolors.WARNING+"  ||   "+ bcolors.ENDC,bcolors.OKBLUE+ "3"+ bcolors.ENDC,)
    print(bcolors.WARNING+ "        ||        ||"+ bcolors.ENDC)
    print("\n")

def checkBoard(board):
    if ' ' in board.values() :
        return True
    else:
        print("REMIS")
        return False

def game(player1,player2):
    p=initGame()
    graphics(p)
    flag=True
    while True:
        p1 = inputVeryfication(player1,"X",p)
        setPosition("X",p1,p)
        flag=checkBoard(p)
        if not flag:
            break
        graphics(p)
        flag = check(p,player1,"X")
        if not flag:
            break
        flag = check(p,player2,"O")
        if not flag:
            break
        p2 = inputVeryfication(player2, "O",p)
        setPosition("O",p2,p)
        flag=checkBoard(p)
        if not flag:
            break
        graphics(p)
        flag=check(p,player1,"X")
        if not flag:
            break
        flag = check(p,player2,"O")
        if not flag:
            break

def beginGame():
    os.system('clear')
    title()
  
    while True:
    #main menu
        menu_select = input(bcolors.OKGREEN+ " Type \'s\' to start new game \n Type \'h\' for help \n Type \'q\' to quit \n:" + bcolors.ENDC)
    #new game
        if menu_select == "s":
            os.system('clear')
            P1=input(bcolors.OKGREEN+ "Enter name for Player One \n :" + bcolors.ENDC)
            P2=input(bcolors.OKGREEN+ "Enter name for Player Two \n :" + bcolors.ENDC)
            #game
            game(P1,P2)
        #help
        elif menu_select == "h":
            os.system('clear')
            help_select = input(bcolors.OKGREEN+ "Type \'r\' for rules or \'i\' for key input \n :" + bcolors.ENDC)
            if help_select == "r":
                os.system('clear')
                print(bcolors.OKGREEN+ "Each player takes a turn and selects a field \n which they wish to place their marker on by \n typing a corresponding number. \n The goal of the game is to place 3 of your markers \n in a straight line (vertical, horizontal or diagonal)." + bcolors.ENDC)
            elif help_select == "i":
                os.system('clear')
                help()
            else:
                print(bcolors.FAIL+"Invalid entry, try again."+ bcolors.ENDC)
                continue
        elif menu_select == "q":
            exit(0)
        else:
            print(bcolors.FAIL+"Invalid entry, try again."+ bcolors.ENDC)
        continue

beginGame()