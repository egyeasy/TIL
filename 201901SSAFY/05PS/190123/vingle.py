array = [list(reversed([1, 2, 3, 4, 5])), list(reversed([6, 7, 8, 9, 10])), list(reversed([11, 12, 13, 14, 15])), list(reversed([16, 17, 18, 19, 20])), list(reversed([21, 22, 23, 24, 25]))]
print(array)


dir_dict = {'east':'south', 'south':'west', 'west':'north', 'north':'east'}
mov_dict = {'east':(0, 1), 'south': (1, 0), 'west': (0, -1), 'north': (-1, 0)}
result =[[1, 1, 1, 1, 1] for i in range(5)]
pres_dir = 'east'
cur_r, cur_c = 0, 1
mov_r, mov_c = mov_dict[pres_dir]
go_len = len(result)
go_num = 1
go_cnt = 0

def is_wall(r, c, lenn, go_num):
    if r+1 >= lenn or r-1 < 0: return True
    if c+1 >= lenn or c-1 < 0: return True
    return False

def change_dir(pres):
    mov_r, mov_c = mov_dict[dir_dict[pres]]

    return mov_r, mov_c

minn = array[0][0]
cnt = 0
new_list = []
for k in range(25):
    min_i = cnt//5
    min_j = cnt%5
    minn = array[min_i][min_j]
    for i in range(cnt//5, len(array)):
        for j in range(len(array[0])):
            if i == cnt//5 and j < cnt%5:
                continue
            if array[i][j] < minn:
                minn = array[i][j]
                array[i][j], array[min_i][min_j] = array[min_i][min_j], array[i][j]
        new_list.append(minn)

    cnt += 1

    if k == 0:
        result[0][0] = minn
        continue
    print(minn, cur_r, cur_c, mov_r, mov_c)
    if not is_wall(cur_r, cur_c, go_len, go_num):
        result[cur_r][cur_c] = minn
    else:
        mov_r, mov_c = change_dir(pres_dir)
        if go_num % 2:
            go_len -= 1
        else:
            go_num += 1
    
    cur_r += mov_r
    cur_c += mov_c


print(array)
print("result: {}".format(result))

new_list =[[1, 1, 1, 1, 1] for i in range(5)]

cnt = 0
i = 0
j = 0
move_i = 0
move_j = 1
for k in range(25):    
    new_list[i][j] = array[k//5][k%5]
    if i == 0 and j == 4:
        move_i = 1
        move_j = 0
    elif i == 4 and j == 4:
        move_i = 0
        move_j = -1
    elif i == 4 and j == 0:
        move_i = -1
        move_j = 0
    elif i == 1 and j == 0:
        move_i = 0
        move_j = 1
    elif i == 1 and j == 3:
        move_i, move_j = 1, 0
    elif i == 3 and j == 3:
        move_i, move_j = 0, -1
    elif i == 3 and j == 1:
        move_i, move_j = -1, 0
    elif i == 2 and j == 1:
        move_i, move_j = 0, 1
        
    i += move_i
    j += move_j

for i in new_list:
    print(i)