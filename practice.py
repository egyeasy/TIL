arr = [1, 2, 3]
n = len(arr)
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=" ")
#     print()

visited = []
def pop():
    return 0

def push(item):
    return 0

def find_next(item):
    return 0
v = 0
w = 0
def dfs(v):
    visited[v] = 1
    while v:
        w = find_next(v)
        if w:
            push(v)
        while w:
            push(w)
            visited[w] = 1
            v = w
            w = find_next(v)
        v = pop()

def dfsR(v):
    if not visited[v]:
        visited[v] = 1
    for i in range(4):
        if not visited[i]:
            dfsR(i)

# backtrack
max_cand = 0
def backtrack(a, k, max_input):
    c = [0] * max_cand
    if k == max_input:
        # do sth ending
        pass
    else:
        k += 1
        num_cand = make_cand(a, k, max_input, c)
        for i in range(num_cand):
            a[k] = c[i]
            backtrack(a, k, max_input)

def make_cand(a, k, max_input, c):
    in_perms = [0] * max_cand

    for i in range(1, k):
        in_perms[arr[i]] = 1

    num_cand = 0
    for i in range(max_cand):
        if not in_perms[i]:
            c[num_cand] = i
            num_cand += 1
    return num_cand



# 연습문제2 - 원소의 합이 10인 부분집합 구하기
cnt = 0

def backtrack2(a, k, sum):
    global cnt
    cnt += 1
    if k == N:
        if sum == 10:
            for i in range(1, 11):
                if a[i] == True:
                    print(i, end=' ')
            print()
    else:
        k += 1
        # 가지치기 추가
        if sum + k <= 10:
            a[k] = 1; backtrack(a, k, sum + k)
        #
        # a[k] = 1; backtrack(a, k, sum + k) # 가지치기 없으면 이 줄 써야
        a[k] = 0; backtrack(a, k, sum)

N = 10
a = [0] * (N + 1)

cnt = 0
backtrack(a, 0, 0)
print("cnt : ", cnt)