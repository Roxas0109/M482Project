
def run(tower):
    col1 = {}
    col2 = {}
    col3 = {}

    i = 0

    #loop
    for x in tower:
        # print(x[0],x[1],x[2])

        if(x[0] not in col1) and (x[1] not in col2) and (x[2] not in col3):
            col1[x[0]] = 1
            col2[x[1]] = 1
            col3[x[2]] = 1
        else:
            if(x[0] in col1):
                col1[x[0]] += 1
                return col1.index(x)
                
            if(x[1] in col2):
                col2[x[1]] += 1
                return col2

            if(x[2] in col3):
                col3[x[2]] += 1
                return col3
        
    return col1, col2, col3
