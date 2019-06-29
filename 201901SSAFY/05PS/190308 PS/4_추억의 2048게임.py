import sys
sys.stdin = open('4.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def change_left(i):
    # print(mat[i])
    for j in range(side_N):
        if not mat[i][j]:
            find_j = j + dy[dir]
            while 0 <= find_j < side_N:
                if mat[i][find_j]:
                    mat[i][j] = mat[i][find_j]
                    mat[i][find_j] = 0
                    # print("part zero like this", mat[i])
                    break
                find_j += dy[dir]
    for j in range(side_N):
        if 0 <= j + dy[dir] < side_N and mat[i][j] and mat[i][j] == mat[i][j + dy[dir]]:
            mat[i][j] *= 2
            mat[i][j + dy[dir]] = 0
    # print("changed like this", mat[i])
    for j in range(side_N):
        if not mat[i][j]:
            if dir == 0:
                find_j = j + dy[dir]
            while 0 <= find_j < side_N:
                if mat[i][find_j]:
                    mat[i][j] = mat[i][find_j]
                    mat[i][find_j] = 0
                    # print("part zero like this", mat[i])
                    break
                find_j += dy[dir]
    # print("zero like this", mat[i])

def change_right(i):
    # print(mat[i])
    for j in range(side_N - 1, -1, -1):
        if not mat[i][j]:
            find_j = j + dy[dir]
            while 0 <= find_j < side_N:
                if mat[i][find_j]:
                    mat[i][j] = mat[i][find_j]
                    mat[i][find_j] = 0
                    # print("part zero like this", mat[i])
                    break
                find_j += dy[dir]
    for j in range(side_N - 1, -1, -1):
        if 0 <= j + dy[dir] < side_N and mat[i][j] and mat[i][j] == mat[i][j + dy[dir]]:
            mat[i][j] *= 2
            mat[i][j + dy[dir]] = 0
    # print("changed like this", mat[i])
    for j in range(side_N - 1, -1, -1):
        if not mat[i][j]:
            find_j = j + dy[dir]
            while 0 <= find_j < side_N:
                if mat[i][find_j]:
                    mat[i][j] = mat[i][find_j]
                    mat[i][find_j] = 0
                    # print("part zero like this", mat[i])
                    break
                find_j += dy[dir]
    # print("zero like this", mat[i])

def change_up(j):
    # print("original")
    # for i in mat:
    #     print(i)
    # print()
    for i in range(side_N):
        if not mat[i][j]:
            find_i = i + dx[dir]
            while 0 <= find_i < side_N:
                if mat[find_i][j]:
                    mat[i][j] = mat[find_i][j]
                    mat[find_i][j] = 0
                    # print("part zero like this")
                    # for i in mat:
                    #     print(i)
                    # print()
                    break
                find_i += dx[dir]
    for i in range(side_N):
        if 0 <= i + dx[dir] < side_N and mat[i][j] and mat[i][j] == mat[i + dx[dir]][j]:
            mat[i][j] *= 2
            mat[i + dx[dir]][j] = 0
    # print("changed like this")
    # for i in mat:
    #     print(i)
    # print()
    for i in range(side_N):
        if not mat[i][j]:
            find_i = i + dx[dir]
            while 0 <= find_i < side_N:
                if mat[find_i][j]:
                    mat[i][j] = mat[find_i][j]
                    mat[find_i][j] = 0
                    # print("part zero like this")
                    # for i in mat:
                    #     print(i)
                    # print()
                    break
                find_i += dx[dir]
    # print("zero like this")
    # for i in mat:
    #     print(i)
    # print()

def change_down(j):
    # print("original")
    # for i in mat:
    #     print(i)
    # print()
    for i in range(side_N - 1, -1, -1):
        if not mat[i][j]:
            find_i = i + dx[dir]
            while 0 <= find_i < side_N:
                if mat[find_i][j]:
                    mat[i][j] = mat[find_i][j]
                    mat[find_i][j] = 0
                    # print("part zero like this")
                    # for i in mat:
                    #     print(i)
                    # print()
                    break
                find_i += dx[dir]
    for i in range(side_N - 1, -1, -1):
        if 0 <= i + dx[dir] < side_N and mat[i][j] and mat[i][j] == mat[i + dx[dir]][j]:
            mat[i][j] *= 2
            mat[i + dx[dir]][j] = 0
    # print("changed like this")
    # for i in mat:
    #     print(i)
    # print()
    for i in range(side_N - 1, -1, -1):
        if not mat[i][j]:
            find_i = i + dx[dir]
            while 0 <= find_i < side_N:
                if mat[find_i][j]:
                    mat[i][j] = mat[find_i][j]
                    mat[find_i][j] = 0
                    # print("part zero like this")
                    # for i in mat:
                    #     print(i)
                    # print()
                    break
                find_i += dx[dir]
    # print("zero like this")
    # for i in mat:
    #     print(i)
    # print()


T = int(input())
for tc in range(1, T + 1):
    side_N, direction = input().split()
    side_N = int(side_N)
    mat = [0] * side_N
    for i in range(side_N):
        mat[i] = list(map(int, input().split()))

    for i in range(side_N):
        if direction == "left":
            dir = 0
            change_left(i)
        elif direction == "right":
            dir = 1
            change_right(i)
        elif direction == "up":
            dir = 2
            change_up(i)
        else:
            dir = 3
            change_down(i)
    print("#{}".format(tc))
    for i in range(side_N):
        for j in range(side_N):
            print(mat[i][j], end=" ")
        print()