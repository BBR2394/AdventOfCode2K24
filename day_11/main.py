#! python3

import sys

sys.path.append("../day_02")
import my_readFile 


def main(av):
    print("Day - 11")

    file = my_readFile.readFile(av[1])

    for i in file:
        print(i)



if __name__ == '__main__':
    main(sys.argv)