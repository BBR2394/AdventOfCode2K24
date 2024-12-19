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

def get_dir(d):
    global list_dir
    if d == '^':
        return list_dir[0]
    elif d == '>':
        return list_dir[1]
    elif d == '<':
        return list_dir[3]
    elif d == 'v':
        return list_dir[2]

def to_moove(mat, instruc):

    for i in instruc:
        dir = get_dir(i)

    for i in mat:
        print(i)

def main(av):
    print("Day - 15")

    #board = my_readFile.createMatrice(av[1])
    board = my_readFile.readFile(av[1])
    
    instruction = board.pop()

    board.pop()
    print("les instruction")
    print(instruction)
    print("le plateau")
    for i in board:
        print(i)
    
    to_moove(board,instruction)

if __name__ == '__main__':
    main(sys.argv)



