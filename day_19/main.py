#! python3

import sys

sys.path.append("../day_02")
import my_readFile 


def work_day_nineteen(pattern, list_data):
    print("les patterns voulus")
    print(pattern)

    print("la list des données")
    for i in list_data:
        print(i)

def main(av):
    print("Day - 19")

    file = my_readFile.readFile(av[1])
    
    work_day_nineteen(file[0], file[2:])


if __name__ == '__main__':
    main(sys.argv)