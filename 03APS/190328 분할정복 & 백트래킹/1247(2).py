import sys
sys.stdin = open('1247.txt', 'r')

min_distance = 0

def swap_perm(n, k):
    if k == n:
        total_distance(clients)
    else:
        for i in range(k, n):
            clients[k], clients[i] = clients[i], clients[k]
            swap_perm(n, k + 1)
            clients[k], clients[i] = clients[i], clients[k]
            

def total_distance(alist):
    global min_distance
    total_distance = 0
    for i in range(N_client):
        if i == 0:
            total_distance += cal_distance(company, alist[i])
            if total_distance > min_distance:
                return
        else:
            total_distance += cal_distance(alist[i - 1], alist[i])
            if total_distance > min_distance:
                return
    total_distance += cal_distance(alist[i], home)
    if total_distance < min_distance:
        min_distance = total_distance


def cal_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


T = int(input())
for tc in range(1, T + 1):
    N_client = int(input())
    nums = list(map(int, input().split()))
    company = nums[:2]
    home = nums[2:4]
    clients = [0] * N_client
    for i in range(N_client):
        clients[i] = nums[4 + i * 2 : 4 + (i + 1) * 2]
    
    min_distance = 1000000000000000

    swap_perm(N_client, 0)

    print(f"#{tc} {min_distance}")