from generators import p1,p2,p3,p4,p5,p6
from collections import deque
from checker import solve
import datetime
from math import comb
from itertools import combinations

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
        calcNum = p1(i+1)

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

def minOb(tower,i):
    comboLen = comb(31, i) # 31 choose i
    combos = list(combinations(tower, i))
    minimumObstacle = False
    for j in range(comboLen):
        comboList = list(combos[j])
        sol = solve(comboList)
        if(sol):
            return minimumObstacle


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


    # tower=[deque([5,3,1]),deque([5,4,2]),deque([6,4,2]),deque([1,5,3]),deque([1,4,2]),deque([6,3,6])]
    
    
    sol=solve(tower)
    print('after solve\n\n\n')

    for i in reversed(range(1,31)):
        print(i)
        res = minOb(tower,i)
        if res:
            print(res)
            break


    end = datetime.datetime.now()
    print("Time =", end - start)
