#! python3

import sys
import my_readFile
from collections import deque

# def order(cur, queue, order):
#     next = queue.popleft()

#     if cur < next !== order:
#         return False
#     else :
        

def check_order(line):
    my_queue = deque(line)
    #print("check order : " , line)
    order = None
    cur = int(my_queue.popleft())
    while len(my_queue) > 0 :
        #print(cur, " : ", my_queue[0])

        if cur == int(my_queue[0]):
            return False
        

        if order == None:
            order = cur < int(my_queue[0])
        elif order == True:
            #print("cur < int(my_queue[0])", cur < int(my_queue[0]))
            if (cur < int(my_queue[0])) == False:
                return False

        elif order == False:
            if (cur < int(my_queue[0])) == True:
                return False
            
        #print("order = ", order)
        cur = int(my_queue.popleft())
    #print("on retrourne true")
    return True

    # next = my_queue[0]
    # order(my_queue.popleft(), my_queue, None)
g_nf_last_faulty = 0
def check_order_step_two(line):
    my_queue = deque(line)
    #print("check order : " , line)
    order = None
    cur = int(my_queue.popleft())
    faulty = 0
    while len(my_queue) > 0 :
        #print(cur, " : ", my_queue[0])
        if cur == int(my_queue[0]):
            faulty += 1
        if order == None:
            order = cur < int(my_queue[0])
        elif order == True:
            #print("cur < int(my_queue[0])", cur < int(my_queue[0]))
            if (cur < int(my_queue[0])) == False:
                faulty += 1

        elif order == False:
            if (cur < int(my_queue[0])) == True:
                faulty += 1
            
        #print("order = ", order)
        cur = int(my_queue.popleft())
    #print("on retrourne true")
    #print("faulty = ", faulty)
    g_nf_last_faulty = faulty
    if faulty > 1 :
        return False
    else: 
        return True

def check_differ(line):
    my_queue = deque(line)
    cur = int(my_queue.popleft())
    while len(my_queue) > 0 :
        diff = abs(int(cur) - int(my_queue[0]))
        if diff > 3 :
            return False
        cur = int(my_queue.popleft())
        
    return True

def check_line(lst):
    finalRes = []
    for i in lst:
        line = i.split(' ')
        check_one = check_order_step_two(line)
        check_two = check_differ(line)
        #check_two = True
        #print("line : ", line, " check 1 : ", check_one, " check 2 : ", check_two)
        finalRes.append(check_one and check_two)
    
    print("resultats finaux : ", finalRes.count(True))


def main(av):
    print("Day 2")
    if len(av) >= 2:
        lst = my_readFile.readFile(av[1])
    else : 
        lst = my_readFile.readFile('')

    check_line(lst)

if __name__ == '__main__':
    main(sys.argv)