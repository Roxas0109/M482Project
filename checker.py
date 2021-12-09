from collections import deque
from dict import slices

def solve(tower):
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
            if(len(sides[1]) == len(tower)):
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
    
    row1 = sides[1]
    row2 = sides[2]
    row3 = sides[3]
    together = []
    for (x,y,z) in zip(row1,row2,row3):
        together.extend((x,y,z))
    together = [deque(together[i:i+3]) for i in range(0, len(together), 3)]
    for x in together:
       print('[%d, %d, %d]'%(x[0],x[1],x[2]))

    return together

