from collections import deque
from dict import slices

def run(tower, size):
    col1 = {}
    col2 = {}
    col3 = {}
    
    solList = []

    i=0

    while(True):
        if(slices[0] > 0):
            print("No Solution")
            break

        if(tower[i][0] not in col1) and (tower[i][1] not in col2) and (tower[i][2] not in col3):
            col1[tower[i][0]] = 1
            col2[tower[i][1]] = 1
            col3[tower[i][2]] = 1
            solList.extend((tower[i][0], tower[i][1], tower[i][2]))
            print("added: [%d, %d, %d]" %
                (tower[i][0], tower[i][1], tower[i][2]))
            if(len(solList) == size):
                break
            i += 1

        elif(tower[i][0] in col1) or (tower[i][1] in col2) or (tower[i][2] in col3):
            while(True):
                if(slices[i] < 2):
                    slices[i] += 1
                    tower[i].rotate()
                    print("rotated slice: %d (%d times)" % (i+1, slices[i]))
                    print("[%d, %d, %d]" %
                    (tower[i][0], tower[i][1], tower[i][2]))
                    break
                else:
                    slices[i] = 0
                    print("popped: [%d, %d, %d]" %
                            (solList.pop(), solList.pop(), solList.pop()))
                    col1.popitem()
                    col2.popitem()
                    col3.popitem()
                    i-=1
                    print("backtracked to slice %d" % (i+1))

    li = [deque(solList[i:i+3]) for i in range(0, len(solList), 3)]
    return li


def solve(tower,size):
    sides = {
        1 : [],
        2 : [],
        3 : []
    }
    #append the first row of tower to dictionary
    sides[1].append(tower[0][0])
    sides[2].append(tower[0][1])
    sides[3].append(tower[0][2])
    i = 1
    while(True):
        if(slices[0] > 0):
            print("No Solution")
            break

        if(tower[i][0] not in sides[1]) and (tower[i][1] not in sides[2]) and (tower[i][2] not in sides[3]):
            sides[1].append(tower[i][0])
            sides[2].append(tower[i][1])
            sides[3].append(tower[i][2])
            if(len(sides[1]) == size):
                break
            i+=1
        elif(tower[i][0] in sides[1]) or (tower[i][1] in sides[2]) or (tower[i][2] in sides[3]):
            while(True):
                if(slices[i] < 2):
                    slices[i] += 1
                    tower[i].rotate()
                    break
                else:
                    slices[i] = 0
                    sides[1].pop()
                    sides[2].pop()
                    sides[3].pop()
                    i-=1
    return sides