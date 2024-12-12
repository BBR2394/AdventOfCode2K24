#! python3

import sys

sys.path.append("../day_02")
import my_readFile 

def split_str(strg):
    one = int(strg[0:int(len(strg)/2+0.2)])
    two = int(strg[int(len(strg)/2+0.2):])
    return [str(one), str(two)]
# param -> str
# return -> []
def compute_elem(e):

    if int(e) == 0:
        return ['1']
    elif len(e) % 2 == 0:
        return split_str(e)
    else :
        res = int(e) * 2024 
        res = str(res)
        return [res]

def check_sub_element(lst):
    new_lst = []
    for i in lst:
        new_lst += compute_elem(i)

    #print(new_lst)

    return new_lst


def return_number_sub_element(lst):
    count = 0
    for i in lst:
        count += compute_elem(i)

    #print(new_lst)

    return new_lst

def main(av):
    print("Day - 11")

    file = my_readFile.readFile(av[1])

    lst = file[0].split(' ')
    for i in lst:
        print(i)
    main_lst = []
    for i in lst:
        main_lst.append(i)

    blink = 25
    
    while blink > 0:

        lst = check_sub_element(lst)
        if blink%5==0:
            print("blink = ", blink)
            print(len(lst))
        blink -= 1

    print(lst)
    print("res final")
    print(len(lst))


if __name__ == '__main__':
    main(sys.argv)