from generators import p1,p2,p3,p4,p5,p6
from collections import deque
from checker import solve
import datetime
from math import comb
from itertools import combinations
from typing import List

# func to generate numbers
def generate():

    # init master list
    masterList = []

    # dictionary to keep track of repetitions
    tracker = {}

    # var for current number being generated
    i = 0

    # loop
    while(True):

        # calc number at current index starting from 1
        calcNum = p6(i+1)

        # if generated num isn't in tracker, add it in array and tracker
        if(calcNum not in tracker):
            tracker[calcNum] = 1
            masterList.append(calcNum)

        # if generated num already exists
        else:
            # check if < 3 occurances, if so increment occurance and add to list
            if(tracker[calcNum] < 3):
                tracker[calcNum] += 1
                masterList.append(calcNum)

        # if length of array = 93, stop loop
        if(len(masterList) == 93):
            break

        # increment
        i += 1

    #create tower list of size 3 to represent slices
    tower = [masterList[i:i+3] for i in range(0, len(masterList), 3)]
    return tower


if __name__ == "__main__":
    #timer
    start = datetime.datetime.now()
    print(start)

    # call func to generate the tower
    tower = generate()
    
    # trys to solve original pizza slice tower
    if not solve([deque(i) for i in tower]):
        print('No solution.')
    print('\n\n\nFinding Minimal Obsticle')

    # Creates combinations starting from 30 to 2 to find the minimal obsticle
    minOb = None
    for i in range(2,len(tower)):
        found = False
        #creats all combinations of size i
        subsets = list(combinations(tower,i))
        print(i)
        for s in subsets:
            #converts s from tuple to list
            s = list(s)
            #converts list to deque
            t = [deque(x) for x in s]
            # calls solve function on t (partial tower). if result is found function is done
            if not solve(t):
                found = True
                print('Found Minimal Obstical of size ' + str(i) + '.')
                for x in s:
                    print(x)
                break
            s.clear()
        if found:
            break
        subsets.clear()

    end = datetime.datetime.now()
    print("Time =", end - start)
