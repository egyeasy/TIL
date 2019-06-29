def make_set(x):
    parents[x] = x


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    parents[find_set(y)] = find_set(x)


def dijkstra(s):
    # U = {s}
    # make_set(s)

    for v in range(1, N + 1):
        D[v] = mat[s][v]
        make_set(v)
    print("D", D)
    # while U != V
    v = -1
    for x in range(1, N + 1):
        if 0 < mat[s][x] < 1000000:
            v = x
            break
    print("v", v)
    visited = [0] * (N + 1)
    visited[s] = 1
    while sum(visited) != N:
        min_idx = -1
        for idx in range(1, N + 1):
            if parents[idx] != parents[s] and not visited[idx]:
                if min_idx == -1:
                    min_idx = idx
                elif D[idx] < D[min_idx]:
                    min_idx = idx

        print("w", min_idx)

        visited[min_idx] = 1
        union(s, min_idx)

        for cand in range(1, N + 1):
            if 0 < mat[min_idx][cand] < 1000000:
                D[cand] = min(D[cand], D[min_idx] + mat[min_idx][cand])

        v = min_idx
        print("D after", D)
        print("visited", visited)



N = 6
M_edges = 9
nnums = '1 2 3 1 3 4 2 4 5 3 2 1 3 4 4 3 5 5 4 5 3 4 6 4 5 6 5'
nums = list(map(int, nnums.split()))
print(nums)
mat = [[1000000] * (N + 1) for _ in range(N + 1)]

for i in range(M_edges):
    mat[nums[i * 3]][nums[i * 3 + 1]] = nums[i * 3 + 2]

for i in range(1, N + 1):
    mat[i][i] = 0

for i in mat:
    print(i)

D = [0] * (N + 1)
parents = [0] * (N + 1)
dijkstra(1)
print(D)