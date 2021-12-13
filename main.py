from generators import p1,p2,p3,p4,p5,p6
from collections import deque
from checker import solve1
import datetime
from math import comb
from itertools import combinations
from typing import List

# func to generate numbers
def generate():

    # init master list
    masterList = []

    # dictionary to keep track of repetitions
    tracker = {}

    # var for current number being generated
    i = 0

    # loop
    while(True):

        # calc number at current index starting from 1
        calcNum = p3(i+1)

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
            break

        # increment
        i += 1
        

    #create tower list with deques of size 3 to represent slices
    tower = [deque(masterList[i:i+3]) for i in range(0, len(masterList), 3)]
    return tower

def minOb(tower,i):
    comboLen = comb(31, i) # 31 choose i
    combos = list(combinations(tower, i))
    #print(combos)
    minimumObstacle = False
    for j in range(comboLen):
        comboList = list(combos[j])
        #print(type(comboList))
        sol = solve(deque(comboList))
        if(sol):
            return minimumObstacle

def find_obstacles(puzzle) -> List[List[int]]:
    """Function to call the solve method on every subset of a given puzzle
       :param puzzle: The puzzle for which we're trying to find a minimum obstacle
       :return The subsets of a puzzle that don't have a solution
    """
    for subset in puzzle:
        global side1, side2, side3
        side1 = []
        side2 = []
        side3 = []
        solution = solve(0, subset)
        if not solution:
            return subset
    return []

def find_minimum_obstacle(puzzle: List[List[int]], upper_bound: int = None) -> List[List[int]]:
    """
    Finds minimum obstacle of a given size
    :param puzzle: The puzzle for which we're trying to find a minimum obstacle
    :param upper_bound: The max size of the minimum obstacle
    :return A list of all minimum obstacles
    """
    if upper_bound is None:
        upper_bound = len(puzzle) + 1
    minimum_obstacle_set: List[List[int]]

    for k in range(2, upper_bound):
        combinations_of_k = combinations(puzzle, k)
        minimum_obstacle_set = find_obstacles(combinations_of_k)
        if len(minimum_obstacle_set) == 0:
            continue
        else:
            return minimum_obstacle_set
    return []

def fix_sides(iteration: int):
    while len(side1) > iteration:
        side1.pop()
        side2.pop()
        side3.pop()


def solve(iteration: int, puzzle: List[List[int]]) -> bool:
    """
    Recursively rotates slices and looks for solutions and stores the, maybe partial, solution in the sides array.
    :param iteration: The number of the block that we're inserting
    :param puzzle: The puzzle that we're trying to solve
    :return True of a solution exists, false otherwise
    """
    if iteration == len(puzzle):
        return True
    if try_insert(iteration, 0, puzzle):
        if solve(iteration + 1, puzzle):
            return True
    if try_insert(iteration, 1, puzzle):
        if solve(iteration + 1, puzzle):
            return True
    if try_insert(iteration, 2, puzzle):
        if solve(iteration + 1, puzzle):
            return True
    return False


def try_insert(iteration: int, side: int, puzzle: List[List[int]]) -> bool:
    """
    Function to insert into the answers array and handle rotations
    :param iteration: The number of the block that we're inserting
    :param side: The side of the slice that we're assuming is "side 1"
    :param puzzle: The puzzle that we're trying to insert into
    :return True of inserting was successful without any conflicts, false otherwise
    """
    fix_sides(iteration)

    if puzzle[iteration][side % 3] in side1:
        return False
    if puzzle[iteration][(side + 1) % 3] in side2:
        return False
    if puzzle[iteration][(side + 2) % 3] in side3:
        return False

    if iteration >= len(side1):
        side1.insert(iteration, puzzle[iteration][side % 3])
        side2.insert(iteration, puzzle[iteration][(side + 1) % 3])
        side3.insert(iteration, puzzle[iteration][(side + 2) % 3])
    else:
        side1[iteration] = puzzle[iteration][side % 3]
        side2[iteration] = puzzle[iteration][(side + 1) % 3]
        side3[iteration] = puzzle[iteration][(side + 2) % 3]


    return True


if __name__ == "__main__":
    #timer
    start = datetime.datetime.now()
    print(start)

    # call func to generate the tower
    tower = generate()
    #for x in tower:
    #    print('[%d, %d, %d]'%(x[0],x[1],x[2]))
    #print(*tower, sep='\n')
    #print('Slices: ', len(tower))


    # tower=[deque([5,3,1]),deque([5,4,2]),deque([6,4,2]),deque([1,5,3]),deque([1,4,2]),deque([6,3,6])]
    
    
    sol= solve1 (tower)
    print('after solve\n\n\n')

    minObsticle = find_minimum_obstacle(list(tower),30)
    print(minObsticle)

    #for i in range(1,31):
    #    print(i)
    #    res = minOb(tower,i)
    #    print(res)
    #    if res:
    #        print(res)
    #        break


    end = datetime.datetime.now()
    print("Time =", end - start)
