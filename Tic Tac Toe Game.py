#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Tic-tac-toe game program
import numpy as np

def printBoard(Board):
    for i in range(3):
        for j in range(3):
            print(Board[i][j],end="|")
        print("\n")
   
def CheckToTerminate(Board):
    Check=True
    for i in Board:
        if "-" in i:
            Check=False
            break
    return Check

def CheckWinner(Board):
    # Check Rows
    for row in [0,1,2]:
        if Board[row][0]!='-' and Board[row][0]==Board[row][1] and             Board[row][1]==Board[row][2]:
                if Board[row][0]=='X':
                    return 1
                else:
                    return 2
                    
    # Check Columns
    for col in [0,1,2]:
        if Board[0][col]!='-' and Board[0][col]==Board[1][col] and             Board[1][col]==Board[2][col]:
                if Board[0][col]=='X':
                    return 1
                else:
                    return 2
    
    # Check forward diagonal
    if Board[0][0]!='-' and Board[0][0]==Board[1][1] and             Board[1][1]==Board[2][2]:
        if Board[0][0]=='X':
            return 1
        else:
            return 2
        
    return 0

# Check backward diagonal
    if Board[0][2]!='-' and Board[0][2]==Board[1][1] and             Board[1][1]==Board[2][0]:
        if Board[0][2]=='X':
            return 1
        else:
            return 2  
              
Board=[["-","-","-"],["-","-","-"],["-","-","-"]]
printBoard(Board)

# Player 1 plays X and player 2 plays O
# Determine the first player
Player=1+round(np.random.random())

Terminate=False
while not Terminate:
    if Player==1:
        print("It is the turn of player ONE")
    elif Player==2:
        print("It is the turn of player TWO")
    else:
        print("Wrong player ID")
        break
    print("Please select the cell you want to play")
    Row,Column= [int(x) for x in input("Enter Row-Column indexes of your tile (space separated): ").split()]
    
    if Player == 1:
        Board[Row-1][Column-1]="X"
    else:
        Board[Row-1][Column-1]="O"
    printBoard(Board)
        
    Winner=CheckWinner(Board)
    if Winner == 1:
        print("Congratulations Player ONE, you WON!")
        break
    elif Winner == 2:
        print("Congratulations Player TWO, you WON!")
        break
    else:
        print("Game Continues")
    
    if Player==1:
        Player=2
    else:
        Player=1
        
    Terminate=CheckToTerminate(Board)
    if Terminate:
        print("The game ended with a TIE")


# In[ ]:





# In[ ]:





# In[ ]:




