def makeset(x):
    parents[x] = x

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    # print("x", find_set(x), "y", find_set(y))
    parents[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    parents = [0] * N
    for i in range(N):
        makeset(i)
    for i in range(len(nums)//2):
        # print(nums[2 * i] - 1, nums[2 * i + 1] - 1)
        union(nums[2 * i] - 1, nums[2 * i + 1] - 1)

    result = []
    for i in range(N):
        result.append(find_set(i))
    # print(result)
    print(f"#{tc} {len(set(result))}")




