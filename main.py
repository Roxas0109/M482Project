from generators import p1,p2,p3,p4,p5,p6
from collections import deque
from checker import solve1
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
        calcNum = p3(i+1)

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

    #create tower list with deques of size 3 to represent slices
    tower = [deque(masterList[i:i+3]) for i in range(0, len(masterList), 3)]
    return tower


if __name__ == "__main__":
    #timer
    start = datetime.datetime.now()
    print(start)

    # call func to generate the tower
    tower = generate()
    #for x in tower:
    #    print('[%d, %d, %d]'%(x[0],x[1],x[2]))
    #print(*tower, sep='\n')
    #print('Slices: ', len(tower))

    # tower with sol.
    # tower=[deque([5,3,1]),deque([5,4,2]),deque([6,4,2]),deque([1,5,3]),deque([1,4,2]),deque([6,3,6])]
    #tower with M.O.
    tower=[deque([1,2,3]),deque([2,1,4]),deque([7,7,2]),deque([5,6,7]),deque([6,5,4])]
    tower=[deque([3, 1, 2]), deque([1, 4, 2]), deque([6, 7, 5]), deque([5, 4, 6])]
    print(tower)
    
    sol= solve1 (tower)
    # print('after solve\n\n\n')

    subsets = list(combinations(tower,4))
    # print(subsets)
    sub = []
    for x in subsets:
    #    print(type(x))
       sub.append(list(x))
       
    # for x in sub:
    #    print(x)
    #    solve1(x)
    print(sub[2])
    s=solve1(sub[2])

    end = datetime.datetime.now()
    print("Time =", end - start)
