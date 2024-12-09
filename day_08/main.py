#! python3

import sys
sys.path.append("../day_02")
import my_readFile 


def main(av):
    print("Day - 08")
    lst = my_readFile.createMatrice(av[1])

    #display_plate(board)

    for i in lst:
        print(i)
    

if __name__ == '__main__':
    main(sys.argv)