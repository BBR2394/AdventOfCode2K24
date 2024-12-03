#! python3

import sys
from collections import deque

import time

my_queue = deque()
res = 0

def read_file(filename):
    fd = None
    print("filename : ", filename)
    if filename:
        fd = open(filename, 'r')
    else:
       fd = open ("./data.txt", 'r')

    input = fd.read()
    return input

def check_parenthesis(cur):
    global my_queue 
    #print("check parenthese : ", cur)
    if cur == '(':
        return True
    else :
        return False

def check_mul(cur):
    global my_queue 
    is_mul = cur + my_queue.popleft() + my_queue.popleft()
    #print("check_mul -> is_mul : ", is_mul)
    if is_mul == "mul":
        return True
    else:
        return False

def get_n_check_firstnum(cur, step, num): # step max is 3
    global my_queue 
    #print("get_n_check_firstnum cur ", cur, " step :  ", step, " num ", num)
    if cur == "," and step == 1:
        return None
    elif cur != "," and step > 3:
        return None
    elif cur == ",":
        #print("ON RETOURNE NUM : ", num)
        return num  

    try :
        int(cur)
    except:
        return None
    #print("on detecte un nombre : ", int(cur))
    tmp = int(cur)

    if step == 1:
        #print("step : ", step, " tmp ", tmp)
        return get_n_check_firstnum(my_queue.popleft(), step+1, tmp)
    if step == 2 or step == 3:
        #print("step : ", step)
        return get_n_check_firstnum(my_queue.popleft(), step+1, num*10 + tmp)

def get_n_check_secondNum(cur, step, num): # step max is 3
    global my_queue 
    #print("get_n_check_firstnum cur ", cur, " step :  ", step, " num ", num)
    if cur == ")" and step == 1:
        return None
    elif cur != ")" and step > 3:
        return None
    elif cur == ")":
        #print("ON RETOURNE NUM : ", num)
        return num  

    try :
        int(cur)
    except:
        return None
    #print("on detecte un nombre : ", int(cur))
    tmp = int(cur)

    if step == 1:
        #print("step : ", step, " tmp ", tmp)
        return get_n_check_secondNum(my_queue.popleft(), step+1, tmp)
    if step == 2 or step == 3:
        #print("step : ", step)
        return get_n_check_secondNum(my_queue.popleft(), step+1, num*10 + tmp)


def my_parser():
    global my_queue 
    global res
    counter_of_mul = 0
    first_num = 0
    second_num = 0
    while len(my_queue) > 0:
        cur = my_queue.popleft()
        print("cur:", cur, end=';')
        if cur == "m":
            print("")
            if check_mul(cur):
                #print("il y a mul : cur : ", cur)
                cur = my_queue.popleft()
                if check_parenthesis(cur):
                    cur = my_queue.popleft()
                    #print("detection de parenthese ok : cur : ", cur)
                    first_num = get_n_check_firstnum(cur, 1, first_num)
                    #print("first_num : ", first_num)
                    cur = my_queue.popleft()
                    #print("cur : ", cur)
                    if first_num != None:
                        second_num = get_n_check_secondNum(cur, 1, second_num)
                        #print("second_num : ", second_num)
                        if second_num != None:
                            res += first_num*second_num
                            print("on arrete pour le moment, first_num :", first_num, "second num: ", second_num, "  res temp ", first_num*second_num, " Res final inter : ", res)
                            counter_of_mul += 1
                            #time.sleep(0.4)

                else : 
                    print("pas de parenthese")
            print("cursor a la fin ", cur)
            #return True
            
    print("nombre de mul : ", counter_of_mul)
    print("resultat final : ", res)
    return True
    
# 14H : 168343063 answer is too low

def lexer_parser(data):
    global my_queue 
    my_queue = deque(data)
    my_parser()
    # cur = my_queue.popleft()
    # while cur:
    #     print(cur, end='')
    #     if cur == "m":

    #     try :
    #         cur = my_queue.popleft()
    #     except:
    #         cur = ""



def main(av):
    print("Hello - day_03")
    print(av)
        
    input = read_file(av[1])
    lexer_parser(input)


    
if __name__ == '__main__':
    main(sys.argv)
