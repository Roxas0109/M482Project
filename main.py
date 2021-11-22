import random as rand
from dict import graph
from generators import p1

tower = []

#given a list finds the repeat numbers themselves not the index
def find_repeat(numbers):
    repeats = []
    seen = set()
    for index,num in enumerate(numbers):
        if num in seen:
            repeats.append(num)
        seen.add(num)
    return repeats

#given 2d list gives the number of the repeat in that list coresponding the the given index
def find_repeat2(tower):
    repeats = [None]*31
    seen = set()
    for index,row in enumerate(tower):
        print(index, row)
        seen = set()
        for num in row:
            if num in seen:
                repeats[index] = num
            seen.add(num)
            graph[num]+=[index]
    return repeats


def rotate(index):
    temp = tower[index][0]
    tower[index][0] = tower[index][1]
    tower[index][1] = tower[index][2]
    tower[index][2] = temp

#generated the tower in 31*3 array, can be switch changing the value of n
def generate():
    n = 3
    masterList = list(range(0,31)) *3
    for i in masterList:
        masterList[i] = p1(i+1)
    print(masterList)
    # rand.shuffle(masterList)
    tower = [masterList[i:i+n] for i in range(0, len(masterList), n)]
    return tower
    



if __name__ == "__main__":
    tower = generate()
    print(tower)
    # print(find_repeat2(tower))
    # print(graph)