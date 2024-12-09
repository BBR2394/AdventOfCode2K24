#! python3

import sys

sys.path.append("../day_02")
import my_readFile 

def add_char(char, occur):
    i = 0
    res = ""
    while i < occur:
        res += char
        i += 1

    return res

def create_first_line(line):
    new_line = ""

    number = 0
    point_or_number = True
    cur = 0
    for i in line:
        cur = int(i)

        if point_or_number:
            new_line += add_char(str(number),cur)
            number += 1
        else:
            new_line += add_char(".",cur)
        point_or_number = not point_or_number

    print("nouvelle ligne : ")
    print(new_line)
    return new_line

def get_index_last_int(line):
    i = 0
    index_last_int = 0
    while i < len(line):
        if line[i] != '.':
            index_last_int = i
        i += 1
    return index_last_int

# warning : numToInsert must be a 'char' (a string)
def replace_first_point(line, numToInsert):
    i = 0
    while i < line:
        if line[i] == '.':
            line[i] = numToInsert
            return
        i += 1



def create_others_line(previousLine, level=0):
    length = len(previousLine)
    last_char = ""
    i = len(previousLine) -1
    while last_char == "" : #or i < 0
        if previousLine[i] != '.':
            last_char = previousLine[i]
            previousLine[i] = '.'
            break
        i -= 1
    print("last char : ", last_char)
    previousLine.replace('.', last_char, 1)
    #previousLine[previousLine.index('.')] = last_char
    return previousLine


def compute_line(line):
    print("la ligne a ordonner")
    print(line)
    lst = []
    firstLine = create_first_line(line)
    lst.append(firstLine)

    print("first ligne ")
    print(firstLine)
    otherLine = firstLine
    first_point = firstLine.index('.')
    last_int = get_index_last_int(firstLine)

    # if first_point < last_int:
    #     otherLine = create_others_line(firstLine)
    #     print("nouvelle ligne")
    #     print(otherLine)

def main(av):
    print("Day - 09")

    line = my_readFile.readFile(av[1])

    compute_line(line[0])


if __name__ == '__main__':
    main(sys.argv)