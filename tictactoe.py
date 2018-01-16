#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 

def initGame():
    board={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
    return board

def setPosition(player, input, board):
    board[str(input)]=player
    return board

def inputVeryfication(player):
    playButtons = [1,2,3,4,5,6,7,8,9]
    while True:
        p=input(str(player) + ": ")
        try:
            p=int(p)
            if p in playButtons:
                break
            else:
                print("Zły przycisk. Ponów próbę")
                continue
        except:
            print("Ponów próbę")
            continue
    return p

def graphics(p):
    print("        ||        ||")
    print("   ",p["1"],"  ||   ",p["2"],"  ||   ",p["3"],)
    print("        ||        ||")
    print("==============================")
    print("        ||        ||")
    print("   ",p["4"],"  ||   ",p["5"],"  ||   ",p["6"],)
    print("        ||        ||")
    print("==============================")
    print("        ||        ||")
    print("   ",p["7"],"  ||   ",p["8"],"  ||   ",p["9"],)
    print("        ||        ||")

def main():
    p=initGame()
    print(p)
    flag=True
    i=0
    graphics(p)

    while flag:
        p1 = inputVeryfication("Player 1")
        setPosition("X",p1,p)
        graphics(p)
        p2 = inputVeryfication("Player 2")
        setPosition("O",p2,p)
        graphics(p)
        i+=1
        if i==5:
            break
main()