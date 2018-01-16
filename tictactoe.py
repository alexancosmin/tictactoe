#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 
def initGame():
    board={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
    return board

def setPosition(player, input, board):
    usedButtons = [1,2,3,4,5,6,7,8,9]
    if input in usedButtons:
        board[str(input)]=player
        return board
    else:
        print("trzeba wpisać ponownie")
        return

def buttonValidation(button):
    try:
        int(button)
        return True
    except:
        print("Zły przycisk")
    return False
    

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
    player1Flag=True
    player2Flag=False

    while flag:
        print(str(i) + str(player1Flag))
        if player1Flag:    
            player1=input("Player 1:")
            player1Flag=buttonValidation(player1)
        
        if player1Flag:
            setPosition("X",int(player1),p)
            graphics(p)
            print(p)
            player1Flag=False
            player2Flag=True
        else:
            #player1Flag=True
            #player2Flag=False
            continue
        
        if player2Flag:    
            player2=input("Player 2:")
            player2Flag=buttonValidation(player2)
            
        
        if player2Flag:    
            setPosition("O",int(player2),p)
            graphics(p)
            print(p)
            player1Flag=True
            player2Flag=False
        else:
            player1Flag=False
            player2Flag=True
            continue
       
        i+=1
        if i==5:
            break
main()