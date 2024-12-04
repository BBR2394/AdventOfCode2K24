#! python3


str_to_find = ['M', 'A', 'S']

import sys
sys.path.append("../day_02")
import my_readFile 

def check_X(e):
    if e == "X":
        return True
    else:
        return False

def check_line_to_rigth(line, pos_char_to_check):
    global str_to_find 
    if len(str_to_find)-1 < pos_char_to_check:
        return True
    try :
        #print("on verifie line[pos_char_to_check] = ", line[pos_char_to_check], " str_to_find[pos_char_to_check] =  ", str_to_find[pos_char_to_check])
        if line[pos_char_to_check] == str_to_find[pos_char_to_check]:
            return check_line_to_rigth(line, (pos_char_to_check + 1))
        else :
            return False
    except IndexError:
        return False
    
def check_line_to_left(line):
    line.reverse()
    #print("REVERSE Line : ", line)
    return check_line_to_rigth(line, 0)

def check_top(mat, curY, curX, pos_char_to_check):
    #print("top")
    global str_to_find 

    if len(str_to_find)-1 < pos_char_to_check:
        return True
    try :
        #print("checkTTop : on verifie lmat[curY][curX] = ", mat[curY][curX], " str_to_find[pos_char_to_check] =  ", str_to_find[pos_char_to_check])
        if mat[curY][curX] == str_to_find[pos_char_to_check]:
            return check_top(mat, curY-1, curX, pos_char_to_check+1)
        return False
    except IndexError:
        return False
    
def check_bottom(mat, curY, curX, pos_char_to_check):
    #print("bottom")
    global str_to_find 

    if len(str_to_find)-1 < pos_char_to_check:
        return True
    try :
        #print("checkBottom : on verifie line[pos_char_to_check] = ", mat[curY][curX], " str_to_find[pos_char_to_check] =  ", str_to_find[pos_char_to_check])
        if mat[curY][curX] == str_to_find[pos_char_to_check]:
            return check_bottom(mat, curY+1, curX, pos_char_to_check+1)
        return False
    except IndexError:
        return False
    
def check_diagonal(mat, curY, curX, pos_char_to_check, dir_x, dir_y):
    #print("Diagonal : dirX", dir_x, " dirY = ", dir_y)
    global str_to_find 

    if len(str_to_find)-1 < pos_char_to_check:
        return True
    try :
        #print("check Diag : on verifie line[pos_char_to_check] = ", mat[curY][curX], " str_to_find[pos_char_to_check] =  ", str_to_find[pos_char_to_check])
        if mat[curY][curX] == str_to_find[pos_char_to_check]:
            return check_diagonal(mat, curY+dir_y, curX+dir_x, pos_char_to_check+1, dir_x, dir_y)
        return False
    except IndexError:
        return False

def pass_through_matrice(mat):
    x = 0
    y = 0
    size_X = len(mat[0])
    size_Y = len(mat)
    cur_x = 0
    cur_y = 0

    count_X = 0
    count_right_xmas = 0
    count_left_xmas = 0
    count_top = 0
    count_bottom = 0

    count_diag_ne = 0
    count_diag_nw = 0
    count_diag_se = 0
    count_diag_sw = 0

    print("DAY04:Matrix Size (x;y) = (", size_X,";", size_Y,").")

    while cur_y < size_Y:
        #print("ligne : ", cur_y)
        #print(mat[cur_y])
        while cur_x < size_X:
            if check_X(mat[cur_y][cur_x]):
                count_X += 1
                #print('1')
                #print(mat[cur_y][cur_x+1:])
                right_check = check_line_to_rigth(mat[cur_y][cur_x+1:], 0)
                #print('2')
                #print(mat[cur_y][0:cur_x])
                left_check = check_line_to_left(mat[cur_y][0:cur_x])

                top_check = check_top(mat, cur_y-1, cur_x, 0)
                bottom_check = check_bottom(mat, cur_y+1, cur_x, 0)

                diag_ne = check_diagonal(mat, cur_y-1, cur_x+1, 0, 1, -1)
                diag_nw = check_diagonal(mat, cur_y-1, cur_x-1, 0, -1, -1)
                diag_se = check_diagonal(mat, cur_y+1, cur_x+1, 0, 1, 1)
                diag_sw = check_diagonal(mat, cur_y+1, cur_x-1, 0, 1, -1)

                if right_check:
                    count_right_xmas += 1
                if left_check:
                    count_left_xmas += 1
                if top_check:
                    count_top += 1
                if bottom_check:
                    count_bottom += 1
                if diag_ne:
                    count_diag_ne += 1
                if diag_nw:
                    count_diag_nw += 1
                if diag_se:
                    count_diag_se += 1
                if diag_sw:
                    count_diag_sw += 1
                #HRE WE DO THE CHECK
            cur_x += 1
        #print("il y a ", count_X, " X sur la ", cur_y, " ligne")

        cur_x = 0
        cur_y += 1
        
        

    print("il y a ", count_X, " X en tout")
    print("il y a : ", count_right_xmas , " Right XMAS")
    print("il y a : ", count_left_xmas , " Left XMAS")
    print("il y a : ", count_top , " Montant XMAS")
    print("il y a : ", count_bottom , " Descendant XMAS")
    print("il y a : ", count_diag_ne , " Diagonal NordEst")
    print("il y a : ", count_diag_nw , " Diagonal NordOuest")
    print("il y a : ", count_diag_se , " Diagonal SudEst")
    print("il y a : ", count_diag_sw , " Diagonal SudOuest")

    res_final = count_right_xmas+count_left_xmas+count_top+count_bottom+count_diag_ne+count_diag_nw+count_diag_se+count_diag_sw
    print("resultat final : ", res_final)

def main(av):
    print("Hello - day_04")
    print(av)


    matrice = my_readFile.createMatrice(av[1])
    # for i in matrice:
    #     print(i)
    pass_through_matrice(matrice)

if __name__ == '__main__':
    main(sys.argv)