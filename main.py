import random as rand
from dict import graph
from generators import p1


# def rotate(index):
#     temp = tower[index][0]
#     tower[index][0] = tower[index][1]
#     tower[index][1] = tower[index][2]
#     tower[index][2] = temp

# generated the tower in 31*3 array, can be switch changing the value of n
# def generate():
#     n = 3
#     masterList = list(range(0,31)) *3
#     for i in masterList:
#         masterList[i] = p1(i+1)
#     print(masterList)
#     tower = [masterList[i:i+n] for i in range(0, len(masterList), n)]
#     return tower

# while list is not done iterate
# if num is not in tracker, add
# if number doesn't have 3 occurances, add to masterList

#func to generate numbers
def generate():
    #init master list
    masterList = []
    #bool for while loop
    done = False
    #dictionary to keep track of repetitions
    tracker = {}
    #var for current number being generated
    i = 0

    #loop
    while(not done):
        #calc number at current index starting from 1
        calcNum = p1(i+1)

        #if generated num isn't in tracker, add it in array and tracker
        if(calcNum not in tracker):
            tracker[calcNum] = 1
            masterList.append(calcNum)
        #if generated num already exists
        else:
            #check if < 3 occurances, is so increment occurance and add to list
            if(tracker[calcNum] < 3):
                tracker[calcNum] += 1
                masterList.append(calcNum)
        #if length of array = 93, stop loop
        if(len(masterList) == 93):
            done = True
        #increment
        i += 1
    print(tracker)
    print(len(tracker.keys()))
    print(masterList)


if __name__ == "__main__":
    #call func to generate the tower
    tower = generate()
    # print(tower)
    # print(find_repeat2(tower))
    # print(graph)
