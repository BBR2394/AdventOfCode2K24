#! python3

import sys
import rulechecker
sys.path.append("../day_02")
import my_readFile 


# res with example is 278 : it works
def get_res_from_computed_rules_list(list):
    finalRes = 0
    for i in list:
        line = i.split(',')
        print(line)
        print(round(len(line)/2 - 0.1 ))
        finalRes += int(line[round(len(line)/2 - 0.1 )])

    print("resultat final : ", finalRes)

def main(av):
    print("Day - 05")
    first_part_list = []
    second_part_list = []
    full_input = my_readFile.readFile(av[1])

    print(full_input)
    tmp = full_input.pop()

    while tmp != '':
        second_part_list.append(tmp)
        tmp = full_input.pop()

    
    print("on a reussi a separer les listes")
    rc = rulechecker.RuleChecker(42)
    print(rc.getNumber())
    #for i in second_part_list:
    #    print(i)


    #get_res_from_computed_rules_list(second_part_list)

if __name__ == '__main__':
    main(sys.argv)