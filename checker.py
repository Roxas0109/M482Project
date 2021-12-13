from collections import deque
from dict import slices

def solve(tower):
    #keeps track of solution in dictionary list
    sides = {
        1 : [],
        2 : [],
        3 : []
    }
    # resets values in slices for new solve check
    for i in range(31):
        slices[i] = 0
    #append the first row of tower to dictionary for faster performance
    sides[1].append(tower[0][0])
    sides[2].append(tower[0][1])
    sides[3].append(tower[0][2])
    i = 1
    while(True):
        # if the first/top slice rotates then there is no solution
        if(slices[0] > 0):
            #print("No Solution")
            # return False
            return
        # if each value of the pizza slice is not on that side append it to the solution
        if(tower[i][0] not in sides[1]) and (tower[i][1] not in sides[2]) and (tower[i][2] not in sides[3]):
            sides[1].append(tower[i][0])
            sides[2].append(tower[i][1])
            sides[3].append(tower[i][2])
            if(len(sides[1]) == len(tower)):
                break
            i+=1
        #if there is a value on that side already, rotate the slice 
        elif(tower[i][0] in sides[1]) or (tower[i][1] in sides[2]) or (tower[i][2] in sides[3]):
            while(True):
                #rotate slice
                if(slices[i] < 2):
                    slices[i] += 1
                    tower[i].rotate()
                    break
                #if rotated twice already backtrack
                else:
                    slices[i] = 0
                    sides[1].pop()
                    sides[2].pop()
                    sides[3].pop()
                    i-=1
    #if solution is found take values from dictionary and put into list
    row1 = sides[1]
    row2 = sides[2]
    row3 = sides[3]
    # together = [list.extend(x,y,z) for (x,y,z) in zip(row1, row2, row3)]
    together = []
    #append the sides to a deque to return and print
    for (x,y,z) in zip(row1,row2,row3):
        together.extend((x,y,z))
    together = [deque(together[i:i+3]) for i in range(0, len(together), 3)]
    #print('Solution Found:')
    #for x in together:
    #   print('[%d, %d, %d]'%(x[0],x[1],x[2]))
    
    return together

