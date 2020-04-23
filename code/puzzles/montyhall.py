#!/usr/bin/python3
import sys
from random import randint

def main():
    '''
     Simulator for the monty hall problem
     Picks a door, opens all but one of the other doors with a goat behind it
     Prints results for switching the choice, sticking with the original choice and randomly picking one of the two doors
     By changing the totalNumberDoors parameter, you can simulate monty hall with different number of doors 
    '''
    totalTries = 100000 
    switchWins =0
    sameWins =0
    randomWins =0
    totalNumberDoors = 3 
    maxDoorNumber  = totalNumberDoors -1
    for _ in range(totalTries):
        doors =[0 for x in range(totalNumberDoors)]
        prizeDoor = randint(0,maxDoorNumber)
        goatDoorNumbers =[0 for x in range(maxDoorNumber)]
        count =0
        for j in range(0,totalNumberDoors):
            if j == prizeDoor:
                doors[j]=1
            else:
                goatDoorNumbers[count]=j
                count+=1

        initialChoice = randint(0,maxDoorNumber)
        
        if initialChoice in goatDoorNumbers:
            goatDoorNumbers.remove(initialChoice)
        goatDoorNumber = goatDoorNumbers[randint(0,len(goatDoorNumbers)-1)]
        doorsAfterOpening =[prizeDoor,goatDoorNumber]

        
        newRandomChoice = doorsAfterOpening[randint(0,len(doorsAfterOpening)-1)]
        newChoice =doorsAfterOpening[0]
        if  doorsAfterOpening[0] == initialChoice:
            newChoice =doorsAfterOpening[1]
        
        if doors[newChoice] ==1:
            switchWins+=1
        if doors[initialChoice] ==1:
            sameWins +=1
        if doors[newRandomChoice] ==1:
            randomWins +=1

    print("Win% with switching ", switchWins*100/totalTries, " Win% by sticking to the same door ", sameWins*100/totalTries, "Win% by randomly choosing a door  ",randomWins*100/totalTries,"%")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
