import sys
sys.stdin = open('matrix.txt', 'r')

def mat_mul(i, j):
    global total_cal
    if i == j:
        return 0
    else:
        min_cal = min([mat_mul(i, k) + mat_mul(k + 1, j) + arranged[i - 1] * arranged[k] * arranged[j] for k in range(i, j)])
        total_cal += min_cal
        print(i, j, min_cal)
        return min_cal

T = int(input())
for tc in range(1, T + 1):
    N_cal = int(input())
    nums = list(map(int, input().split()))
    arranged = []
    arranged.append(nums[0])
    for i in range(N_cal):
        arranged.append(nums[2 * i + 1])
    print(arranged)
    total_cal = 0
    mat_mul(1, N_cal)
    print(total_cal)

    print()