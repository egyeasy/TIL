import sys
sys.stdin = open("3.txt", "r")

def DFSr(start):
    global t_end, judge
    v = start
    visited[v] = 1
    # print(v)
    if v == t_end:
        judge = True
        return
    for i in range(num_node + 1):
        if matrix[v][i] and not visited[i]:
            DFSr(i)

T = int(input())
for tc in range(1, T+1):
    num_node, num_edge = map(int, input().split())
    matrix = [[0] * (num_node + 1) for i in range(num_node + 1)]
    visited = [0] * (num_node + 1)

    for i in range(num_edge):
        start, end = map(int, input().split())
        matrix[start][end] = 1

    t_start, t_end = map(int, input().split())

    # print(matrix)
    judge = False

    DFSr(t_start)

    print(f"#{tc} {judge*1}")
