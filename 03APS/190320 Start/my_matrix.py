import sys
sys.stdin = open('matrix.txt', 'r')

# total_cal = 0
# 
# def mat_mul(i, j):
#     global total_cal
#     if i == j:
#         return 0
#     else:
#         min_cal = min([mat_mul(i, k) + mat_mul(k + 1, j) + arranged[i - 1] * arranged[k] * arranged[j] for k in range(i, j)])
#         total_cal += min_cal
#         print(i, j, min_cal)
#         return min_cal

T = int(input())
for tc in range(1, T + 1):
    N_cal = int(input())
    nums = list(map(int, input().split()))
    arranged = []
    arranged.append(nums[0])
    for i in range(N_cal):
        arranged.append(nums[2 * i + 1])
    # print(arranged)
    
    
    # total_cal = 0
    # mat_mul(1, N_cal)
    # print(total_cal)
    MAX_SIZE = 10
    mat = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    max_value = 99999999999
    result = []
    for diagonal in range(N_cal):
        min_value = max_value
        min_idx = 0
        for i in range(1, N_cal - diagonal + 1):
            j = i + diagonal
            if j == i:
                continue
            mat[i][j] = max_value
            for k in range(i, j):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k + 1][j] + arranged[i - 1] * arranged[k] * arranged[j])
            if mat[i][j] < min_value:
                min_value = mat[i][j]
                min_idx = i, j
        if diagonal:
            result.append(min_idx)
            # print(min_idx, end=" ")
    # print()
        

    # for i in range(10):
    #     if i:
    #         print(mat[i])

    # print(result)
    for i in range(N_cal - 1):
        if not i:
            print(result[i][0], end=" ")
        else:
            if result[i][0] == former[0]:
                print(result[i][1], end=" ")
            else:
                print(result[i][0], end=" ")
        former = result[i]
    print()
    # print()