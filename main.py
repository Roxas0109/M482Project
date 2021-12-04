import random as rand
from dict import graph
from generators import p1,p2,p6
from collections import deque
from checker import run

# func to generate numbers


def generate():
    # init master list
    masterList = []
    # bool for while loop
    done = False
    # dictionary to keep track of repetitions
    tracker = {}
    # var for current number being generated
    i = 0

    # loop
    while(not done):
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
            done = True
        # increment
        i += 1

    #create tower list with deques of size 3 to represent slices
    tower = [deque(masterList[i:i+3]) for i in range(0, len(masterList), 3)]
    return tower


if __name__ == "__main__":
    # call func to generate the tower
    tower = generate()
    # for x in tower:
    #     print('[%d, %d, %d]'%(x[0],x[1],x[2]))
    # print(*tower, sep='\n')
    # print('Slices: ', len(tower))


    tower=[deque([5,3,1]),deque([5,4,2]),deque([2,6,4]),deque([3,1,5]),deque([1,4,2]),deque([6,6,3])]
    # tower=[deque([6,3,6]),deque([1,4,2]),deque([1,5,3]),deque([6,4,2]),deque([5,4,2]),deque([5,3,1])]
    sol=run(tower)

    for x in sol:
        print('[%d, %d, %d]'%(x[0],x[1],x[2]))




    #rotate first slice
    # tower[0].rotate()
