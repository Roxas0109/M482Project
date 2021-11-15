import random as rand

s1 = []
s2 = []
s3 = []

def find_repeat(numbers):
    seen = set()
    for index,num in enumerate(numbers):
        if num in seen:
            return num
        seen.add(num)
    return 32


def rotate(index):
    temp = s1[index]
    s1[index] = s2[index]
    s2[index] = s3[index]
    s3[index] = temp




def generate():
    masterList = list(range(0,6)) *3
    rand.shuffle(masterList)
    #s1 = masterList[:31]
    #s2 = masterList[31:62]
    #s3 = masterList[62:]
    
    s1 = masterList[:6]
    s2 = masterList[6:12]
    s3 = masterList[12:]
    print(find_repeat(s1), s1)
    print(find_repeat(s2), s2)
    print(find_repeat(s3), s3)



if __name__ == "__main__":
    generate()