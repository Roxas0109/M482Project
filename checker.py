from collections import deque
def run(tower):
    col1 = {}
    col2 = {}
    col3 = {}
    rotation = {}
    solList = []

    i = 0
    done = False
    rot = 0

    while(not done):

        if(tower[i][0] not in col1) and (tower[i][1] not in col2) and (tower[i][2] not in col3):
            col1[tower[i][0]] = 1
            col2[tower[i][1]] = 1
            col3[tower[i][2]] = 1
            solList.extend((tower[i][0],tower[i][1],tower[i][2]))
            if(len(solList) == 18):
                done = True
            i+=1
            
        else:
            if(rot < 2):
                rot+=1
                tower[i].rotate()
            else:
                done = True 


    li = [deque(solList[i:i+3]) for i in range(0, len(solList), 3)]
    return li
            
    
