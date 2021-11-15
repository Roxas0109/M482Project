import random as rand

tower = []

def find_repeat(numbers):
    seen = set()
    for index,num in enumerate(numbers):
        if num in seen:
            return num
        seen.add(num)
    return 32


def rotate(index):
    temp = tower[index][0]
    tower[index][0] = tower[index][1]
    tower[index][1] = tower[index][2]
    tower[index][2] = temp




def generate():
    n = 31
    masterList = list(range(0,31)) *3
    rand.shuffle(masterList)
    sublists = [masterList[i:i+n] for i in range(0, len(masterList), n)]
    print(sublists)



if __name__ == "__main__":
    generate()