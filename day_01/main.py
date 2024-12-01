#! python3

import sys
import re


def readFile(av):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    lst_one = []
    lst_two = []
    for i in lst:
        temp = i.split(' ')
        print(temp)
        lst_one.append(temp[0]) 
        lst_two.append(temp[3]) 

    print(lst_two)
    fd.close()


def main(av):
    print("Hello - day_01")
    print(av)
    if len(av) >= 2:
        readFile(av)
    
if __name__ == '__main__':
    main(sys.argv)
