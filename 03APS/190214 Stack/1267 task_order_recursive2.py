import sys
sys.stdin = open("task.txt", "r")

def DFSr(start):
    global idx, length, origin
    v = start
    visited[v] = True
    for i in range(1, length+1):
        if matrix[v][i] == 1 and visited[i] != True:
            DFSr(i)
    # print(f" {v}", end="")
    result[idx] = v
    idx += 1
    # 여기 find_origin() 안 쓰고 matrix 전치로 해결해보려 했는데 안 되겠다
    if v == origin:
        for i in range(1, length+1):
            if matrix[i][v] == 1 and not visited[i]:
                origin = i
                break
        DFSr(origin)

def find_origin():
    global length, matrix
    for point in range(1, length+1):
        if not visited[point]:
            for i in range(1, length+1):
                if matrix[i][point]:
                    break
            else:
                return point

for tc in range(1, 11):
    v, e = map(int, input().split())
    ad_list = list(map(int, input().split()))
    matrix = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    length = v
    ad_len = len(ad_list)
    result = [0]*v
    idx = 0
    for i in range(1, ad_len, 2):
        start = ad_list[i]
        end = ad_list[i-1]
        matrix[start][end] = 1

    # print(ad_list)
    # print(v, e)
    # print(matrix)
    point = find_origin()
    origin = point
    # print("point: {}".format(point))
    DFSr(point)
    print(f"#{tc} {' '.join(map(str, result))}")

