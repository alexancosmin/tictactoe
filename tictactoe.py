#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
                    print("To pole jest już zajęte. Ponów próbę!")
                    continue
                else:
                    break
            else:
                print("Należy podać cyfrę od 1 - 9. Ponów próbę!")
                continue
        except:
            print("Wpisałeś dziwny znak! Należy podać cyfrę od 1 - 9. Ponów próbę!")
            continue
    return p

def graphics(p):
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

def checkx(p,P1,P2):
    if p["1"]=="X" and p["2"]=="X" and p["3"]=="X":
        print(bcolors.FAIL+P1," WIN!"+bcolors.ENDC)
        exit(0)
    elif p["4"]=="X" and p["5"]=="X" and p["6"]=="X":
        print(P1," WIN!")
        exit(0)
    elif p["7"]=="X" and p["8"]=="X" and p["9"]=="X":
        print(P1," WIN!")
        exit(0)
    elif p["1"]=="X" and p["4"]=="X" and p["7"]=="X":
        print(P1," WIN!")
        exit(0)
    elif p["2"]=="X" and p["5"]=="X" and p["8"]=="X":
        print(P1," WIN!")
        exit(0)
    elif p["3"]=="X" and p["6"]=="X" and p["9"]=="X":
        print(P1," WIN!")
        exit(0)
    elif p["1"]=="X" and p["5"]=="X" and p["9"]=="X":
        print(P1," WIN!")
        exit(0)
    elif p["3"]=="X" and p["5"]=="X" and p["7"]=="X":
        print(P1," WIN!")
        exit(0)

def checko(p,P1,P2):
    if p["1"]=="O" and p["2"]=="O" and p["3"]=="O":
        print(P2," WIN!")
        exit(0)
    elif p["4"]=="O" and p["5"]=="O" and p["6"]=="O":
        print(P2," WIN!")
        exit(0)
    elif p["7"]=="O" and p["8"]=="O" and p["9"]=="O":
        print(P2," WIN!")
        exit(0)
    elif p["1"]=="O" and p["4"]=="O" and p["7"]=="O":
        print(P2," WIN!")
        exit(0)
    elif p["2"]=="O" and p["5"]=="O" and p["8"]=="O":
        print(P2," WIN!")
        exit(0)
    elif p["3"]=="O" and p["6"]=="O" and p["9"]=="O":
        print(P2," WIN!")
        exit(0)
    elif p["1"]=="O" and p["5"]=="O" and p["9"]=="O":
        print(P2," WIN!")
        exit(0)
    elif p["3"]=="O" and p["5"]=="O" and p["7"]=="O":
        print(P2," WIN!")
        exit(0)

def help():
    print("\n")
    print(" Key input:")
    print("\n")
    print("        ||        ||")
    print("    7   ||    8   ||   9")
    print("        ||        ||")
    print("==============================")
    print("        ||        ||")
    print("    4   ||    5   ||   6")
    print("        ||        ||")
    print("==============================")
    print("        ||        ||")
    print("    1   ||    2   ||   3")
    print("        ||        ||")
    print("\n")

def game(player1,player2):
    p=initGame()
    flag=True
    i=0
    graphics(p)
    while flag:
        p1 = inputVeryfication(player1,"X",p)
        setPosition("X",p1,p)
        graphics(p)
        checkx(p,player1,player2)
        checko(p,player1,player2)
        p2 = inputVeryfication(player2, "O",p)
        setPosition("O",p2,p)
        graphics(p)
        checkx(p,player1,player2)
        checko(p,player1,player2)
        i+=1
        if i==5:
            break

def beginGame():
    print("\n")
    print(bcolors.OKGREEN+ " Welcome to Tic-Tac-Toe ver. 1.5!" + bcolors.ENDC)

    while True:
    #main menu
        menu_select = input(bcolors.OKGREEN+ " Type \'s\' to start new game \n Type \'h\' for help \n :" + bcolors.ENDC)
    #new game
        if menu_select == "s":
            P1=input(bcolors.OKGREEN+ "Enter name for Player One \n :" + bcolors.ENDC)
            P2=input(bcolors.OKGREEN+ "Enter name for Player Two \n :" + bcolors.ENDC)
            #game
            game(P1,P2)
        #help
        elif menu_select == "h":
            help_select = input(bcolors.OKGREEN+ "Type \'r\' for rules or \'i\' for key input \n :" + bcolors.ENDC)
            if help_select == "r":
                print(bcolors.OKGREEN+ "Each player takes a turn and selects a field \n which they wish to place their marker on by \n typing a corresponding number. \n The goal of the game is to place 3 of your markers \n in a straight line (vertical, horizontal or diagonal)." + bcolors.ENDC)
            elif help_select == "i":
                help()


def main():
    beginGame()
    
main()