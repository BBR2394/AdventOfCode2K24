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

def get_index_last_contigous_int(line):
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

def create_other_lines_list(previousLine, level=0):
    length = len(previousLine)
    first_point = previousLine.index('.')
    last_int = get_index_last_contigous_int(previousLine)
    # print("create other lines list")
    # print(first_point)
    # print(last_int)
    previousLine[first_point] = previousLine[last_int]
    
    previousLine[last_int] = '.'

    return previousLine

def compute_line(line):
    print("la ligne a ordonner")
    print(line)
    lst = []
    firstLine = create_first_line(line)


    fisrt_line_lst = []
    for i in firstLine:
        fisrt_line_lst.append(i)
    

    print("first ligne ")
    print(len(fisrt_line_lst))
    # print(fisrt_line_lst)
    otherLine = firstLine
    first_point = firstLine.index('.')
    last_int = get_index_last_contigous_int(firstLine)

    line_to_copute = fisrt_line_lst
    lst.append(fisrt_line_lst)
    print("on rentre dans le while")
    log_int = 0
    while first_point < last_int:
        otherLine = create_other_lines_list(line_to_copute)
        lst.append(otherLine)
        # print("nouvelle ligne")
        # print(otherLine)
        # print(first_point)
        # print(last_int)
        # print(len(lst))
        if log_int % 100 == 0:
            print("log int du while : ", str(log_int))
        log_int += 1
        line_to_copute = lst[len(lst)-1]
        first_point = line_to_copute.index('.')
        last_int = get_index_last_contigous_int(line_to_copute)

    print("end")
    # print(line_to_copute)

    final_res = 0
    i = 0
    while i < len(line_to_copute):
        if line_to_copute[i] == '.':
            break
        final_res += i* int(line_to_copute[i])

        i += 1

    print("resultat finale : ", str(final_res))

def main(av):
    print("Day - 09")

    line = my_readFile.readFile(av[1])

    compute_line(line[0])


if __name__ == '__main__':
    main(sys.argv)