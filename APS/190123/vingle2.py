result = [[0 for i in range(5)] for i in range(5)]




next_dict = {'west': 'south', 'south': 'east', 'east': 'north',
             'north': 'west'}
mov_dict = {'east': (0, 1), 'south': (1, 0), 'west': (0, -1),
            'north': (-1, 0)}



x, y = (2, 1)
i = 0
j = -1
pres_dir = 'west'
change_num = -1

cnt = 1
n = 1

result[2][2] = 25

for k in range(24, 0, -1):
    result[x][y] = k
    if cnt == n:
        next = next_dict[pres_dir]
        pres_dir = next
        i, j = mov_dict[next]
        x += i
        y += j
        cnt = 1
        change_num += 1
        if change_num % 2:
            n += 1
    else:
        x += i
        y += j
        cnt += 1

for row in result:
    print(row)