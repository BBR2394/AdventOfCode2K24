#! python3

import sys

def readFile(filename):
    fd = None
    print("filename : ", filename)
    if filename:
        fd = open(filename, 'r')
    else:
       fd = open ("./data.txt", 'r')

    input = fd.read()
    lst = input.split('\n')

    return lst


def createMatrice(filename):
    lines = readFile(filename)
    matrice = []
    for i in lines:
        one_line = []
        for e in i:
            one_line.append(e)
        matrice.append(one_line)

    return matrice
              

def main(av):
    print("TEST My lib : readfile")
    print(av)
    lst = []
    if len(av) >= 2:
        lst = readFile(av[1])
    else : 
        lst = readFile('')
    
    print(lst)

if __name__ == '__main__':
    main(sys.argv)