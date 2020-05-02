#!/usr/bin/python3
import sys
import random
from random import randint

def main():
    '''
    https://fivethirtyeight.com/features/can-you-beat-the-goat-monty-hall-problem/
    Monty changes the rules. First, he will randomly pick a number of goats 
    to put behind the doors:zero, one, two or three, each with a 25 percent 
    chance. After the number of goats is chosen, they are assigned to the doors
    at random, and each door has at most one goat. Any doors that don’t have
    a goat behind them have an identical prize behind them.
    At this point, you choose a door. 
    If Monty is able to open another door, revealing a goat, he will do so. 
    But if no other doors have goats behind them, he will tell you that is the case.
    It just so happens that when you play,
    Monty is able to open another door, revealing a goat behind it. 
    Should you stay with your original selection or switch? 
    And what are your chances of winning the prize?
    '''
    totalTries = 100000
    switchWins =0
    sameWins =0
    totalNumberDoors = 3 
    maxDoorNumber  = totalNumberDoors -1
    actualAttempts=0
    for _ in range(totalTries):
        doors =[1 for x in range(totalNumberDoors)]
        #There is atleast one goat in the particular case in the question
        totalNumberOfGoats = randint(1,totalNumberDoors)
        for i in range(0,totalNumberOfGoats):
            doors[i]=0
        # populate array with goats and cars and then shuffle it
        # 1 is the car and 0 is the goat
        random.shuffle(doors)
        goatdoornumbers = [index for index,value in enumerate(doors)  if value ==0]
        firstchoice = randint(0,maxDoorNumber)
        if firstchoice in goatdoornumbers:
           goatdoornumbers.remove(firstchoice)
        if len(goatdoornumbers)==0:
            #one goat game and it was selected but it wasnt the puzzle's scenario
            continue
        openeddoornumber = goatdoornumbers[randint(0,len(goatdoornumbers)-1)]
        if(doors[openeddoornumber]!=0):
            raise ValueError("Opened a door which isnt a goat!")
        doornumbers =[index for index,value in enumerate(doors)]
        doornumbers.remove(openeddoornumber)
        doornumbers.remove(firstchoice)
        secondchoice = doornumbers[randint(0,len(doornumbers)-1)]
        actualAttempts+=1
        
        if doors[secondchoice] ==1:
            switchWins+=1
        if doors[firstchoice] ==1:
            sameWins +=1
    print("Win% with switching ", switchWins*100/actualAttempts, " Win% by sticking to the same door ", sameWins*100/actualAttempts)
    '''
     Switching results in a 50% win rate in this version of the monty hall problem
     Even increasing the number of doors doesnt affect this result
    '''

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
