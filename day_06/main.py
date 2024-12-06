#! python3

import sys

sys.path.append("../day_02")
import my_readFile 

number_of_moov = 0
list_dir = ['North', 'East', 'South','West']
debug = False

direction_object  = { 
    "North": {
        "x":0, 
        "y":-1
        }, 
    "East": {
        "x":1, 
        "y":0
        },
    "West": {
        "x":-1, 
        "y":0
        },
    "South": {
        "x":0, 
        "y":1   
    }
}

def is_current_pos(elem):
    if elem == '^':
        return True
    elif elem == '>':
        return True
    elif elem == '<':
        return True
    elif elem == 'v':
        return True
    else :
        return False

def get_initial_position(mat):
    x = 0
    y = 0

    while y < len(mat):
        while x < len(mat[y]):
            if is_current_pos(mat[y][x]):
                return {'x': x, 'y': y}
            x += 1
        y += 1
        x = 0 
    return {'x': -1, 'y': -1}

def can_moove_next(mat, curDir, curPos):
    next_x = curPos['x'] + direction_object[curDir]['x']
    next_y = curPos['y'] + direction_object[curDir]['y']

    if next_x < 0:
        return False
    elif next_x >= len(mat[0]):
        return False
    elif next_y < 0:
        return False
    elif next_y >= len(mat):
        return False
    else :
        return True

def next_pos(mat, curDir, curPos):
    next_x = curPos['x'] + direction_object[curDir]['x']
    next_y = curPos['y'] + direction_object[curDir]['y']

    return mat[next_y][next_x]

def display_plate(mat, display_anyway=False):
    if debug == True or display_anyway:
        for i in mat:
            print(i)

def go(mat, curDir, curPos):
    # on se deplace

    while can_moove_next(mat, curDir, curPos):
        # print("cur dir : ", curDir, " cur pos : ", curPos)
        try:
            nxt = next_pos(mat, curDir, curPos)
        except:
            print("ERREUR : ")
            display_plate(mat, True)
            print(curPos)
            print(curDir)
            print(can_moove_next(mat, curDir, curPos))
            exit

        if nxt == "#":
            # print("on s'errete pour le moment")
            # print(curPos)
            if curDir == 'North':
                mat[curPos['y']][curPos['x']] = '>'
            elif curDir == 'South':
                mat[curPos['y']][curPos['x']] = 'V'
            if list_dir.index(curDir)+1 >= len(list_dir):
                curDir = list_dir[0]
            else :
                curDir = list_dir[list_dir.index(curDir)+1]
            # print("new dir : ", curDir)
            # display_plate(mat)
            #go(mat, curDir, curPos)
        else :
            mat[curPos['y']][curPos['x']] = 'X'
            curPos['x'] = curPos['x'] + direction_object[curDir]['x']
            curPos['y'] = curPos['y'] + direction_object[curDir]['y']
            mat[curPos['y']][curPos['x']] = '^'
            #return go(mat, curDir, curPos)
    mat[curPos['y']][curPos['x']] = 'X'
    return mat


def count_X(mat):
    count = 0
    for i in mat:
        count += i.count('X')
    return count

def to_guard(mat):
    currentDir = "North"

    curPos = get_initial_position(mat)
    print("la posision intitial")
    print(curPos)

    mat = go(mat, currentDir, curPos)

    print(count_X(mat))


def main(av):
    print("Day - 06")
    board = my_readFile.createMatrice(av[1])

    #display_plate(board)

    to_guard(board)

if __name__ == '__main__':
    main(sys.argv)