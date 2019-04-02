import sys
sys.stdin = open('3752.txt', 'r')

from collections import deque

def bfs(s):
    global cnt
    dq.append(s)
    while dq:
        s = dq.popleft()
        idx = s[0]
        summ = s[1]
        if idx == N_nums:
            break
        # print("idx", idx, "summ", summ)
        for i in range(2):
            if idx < N_nums:
                new_sum = summ + i * nums[idx]
                if not visited[new_sum]:
                    cnt += 1
                    dq.append([idx + 1, new_sum])
                else:
                    if idx + 1 != visited[new_sum]:
                        dq.append([idx + 1, new_sum])
                visited[new_sum] = idx + 1


T = int(input())
for tc in range(1, T + 1):
    N_nums = int(input())
    nums = list(map(int, input().split()))
    dq = deque()
    visited = [0] * 10001
    cnt = 0

    # result = []
    bfs([0, 0])
    # for i in range(100):
    #     print(i + 1, end=" ")
    print(f"#{tc} {cnt}")