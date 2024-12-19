#! python3

import sys

sys.path.append("../day_02")
import my_readFile 

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

def check_case(case):
    if case == "#":
        return False
    else :
        return True

def find_path(mat, x, y):
    mat[y][x] = "O"

    reach_end = False
    
    # while reach_end == False:
    #     check_case()

def fill_mat(coord):
    lst = ['.'] * 7
    
    #mat = [lst] * 10
    mat = []
    r = 0
    while r < 7:
        mat.append(['.'] * 7)
        r += 1

    i = 0 

    while i < 12:
        #temp = i.split(',')
        temp = coord[i].split(',')
        x = int(temp[0])
        y = int(temp[1])
        # print(temp)
        # print(x)
        # print(y)
        # print(mat[y][x])
        mat[y][x] = '#'
        # print(mat[y][x])
        i += 1


    for i in mat:
        print(i)

    find_path(mat)

def main(av):
    print("Day - 18")

    file = my_readFile.readFile(av[1])
    

    fill_mat(file)

    


if __name__ == '__main__':
    main(sys.argv)