from collections import deque

def dfs(s):
    dq.append(s)
    while dq:
        s = dq.pop()
        if not visited[s]:
            print(s, end=" ")
            visited[s] = 1
            for w in ad_list[s]:
                if not visited[w]:
                    dq.append(w)


N = 7
nums = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

ad_list = [[] for _ in range(N + 1)]

for i in range(0, len(nums) - 1, 2):
    ad_list[nums[i]].append(nums[i + 1])
    ad_list[nums[i + 1]].append(nums[i])

for i in ad_list:
    print(i)

dq = deque()
visited = [0] * (N + 1)
dfs(1)
