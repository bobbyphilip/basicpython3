#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
from random import randint

def main():
    '''
    4 prisoners isolated in cells in a castle. They are given a fair coin, and the choice to toss it.
    If all tosses attempted are heads, they will all be  released.
    If no one attempts it or someone tosses a tail, they will stay imprisoned.
    They are given a random number generator.
    https://fivethirtyeight.com/features/can-you-flip-your-way-to-freedom/
    '''
    '''
    Pick a number betwwen 0 and 100. Everyone generates a random number between 0 and 100.
    If it is >= the picked number, toss the coin. 
    If picked number is 0, then everyone will toss, escape change of 1/(2^4)
    If picked number is 100, then no one will toss, and chance is 0%
    Somewhere in middle is the optimal number
    '''
    reps = 10000
    numberofprisoners = 4
    wincount = [0 for i in range(0,100)]
    for baselinenumber in range(0,100):
        for repcounter in range(0, reps):
            win=False
            for i in range(0, numberofprisoners):
                generatednumber = randint(0, 99)
                if generatednumber >= baselinenumber:
                    heads = randint(0, 1)
                    if heads:
                        win = True
                    else:
                        win = False
                        break
            if win:
                wincount[baselinenumber] += 1
    winpercent = [x*100/reps for x in wincount]
    highestIndex =0
    highestValue =0
    for i in range(0,100):
            winrate = winpercent[i]
            if winrate>highestValue:
                highestValue = winrate
                highestIndex = i
    print(winpercent)
    print(' best number choice is ',highestIndex, ' and the win rate is ',highestValue)
    plt.plot(winpercent)
    plt.ylabel('Success possibilty')
    plt.xlabel('number generated')
    plt.show()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
