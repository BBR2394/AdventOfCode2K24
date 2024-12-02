#! python3

import sys
import re

def do_step_two(lst_one, lst_two):
    x = 0
    res = []
    print("lst_one[x] : ", lst_one[x])
    while x < len(lst_one):
        tmp = 0

        nb_occur = lst_two.count(lst_one[x])
        tmp = lst_one[x] * nb_occur
        print("A:", lst_one[x], " et occurence de one dans list_two : ", nb_occur, " et resultat = ", tmp)
        res.append(tmp)
        x += 1

    finalRes = 0
    for k in res:
        finalRes += k
    print("finalRes = ", finalRes)


def readFile(av):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    lst_one = []
    lst_one_int = []

    lst_two = []
    lst_two_int = []
    for i in lst:
        temp = i.split(' ')
        
        lst_one.append(temp[0]) 
        lst_two.append(temp[3]) 

    for j in lst_one:
        lst_one_int.append(int(j))
    for j in lst_two:
        lst_two_int.append(int(j))
    print(lst_one_int)

    step = 2
    if step == 2:
        do_step_two(lst_one_int, lst_two_int)
        return 0
    else :
        lst_one_int.sort()
        lst_two_int.sort()
        print(lst_two_int)
        fd.close()
        x = 0
        res = []
        print("lst_one_int[x] : ", lst_one_int[x])
        while x < len(lst_one_int):
            tmp = 0
            print("lst_one_int[x] : ", lst_one_int[x])
            print("lst_two_int[x] : ", lst_two_int[x])

            if (lst_one_int[x] > lst_two_int[x]):
                tmp = lst_one_int[x] - lst_two_int[x]
            elif (lst_one_int[x] < lst_two_int[x]):
                tmp = lst_two_int[x] - lst_one_int[x]
            else : 
                print("erreur")
            res.append(tmp)
            print("A:", lst_one_int[x], " et ", lst_two_int[x], " et difference = ", tmp)
            x += 1

        finalRes = 0
        for k in res:
            finalRes += k
        print("finalRes = ", finalRes)

def main(av):
    print("Hello - day_01")
    print(av)
    if len(av) >= 2:
        readFile(av)
    
if __name__ == '__main__':
    main(sys.argv)
