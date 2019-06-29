import sys
sys.stdin = open("task.txt", "r")

for tc in range(1, 11):
# for tc in range(1, 2):
    v, e = map(int, input().split())
    ad_list = list(map(int, input().split()))
    matrix = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    length = v
    ad_len = len(ad_list)
    result = [0]*v
    idx = 0
    for i in range(0, ad_len, 2):
        start = ad_list[i]
        end = ad_list[i+1]
        matrix[start][end] = 1

    # print(ad_list)
    # print(v, e)
    # print(matrix)

    while True:
        for start in range(1, length+1):
            if not visited[start]:
                all_zero = True
                for end in range(1, length+1):
                    if matrix[end][start]:
                        all_zero = False
                        break
                if all_zero == True:
                    result[idx] = start
                    idx += 1
                    visited[start] = 1
                    for end in range(1, length+1):
                        matrix[start][end] = 0
            # print(result)
        if idx == length:
            # print(result)
            break
    print(f"#{tc} {' '.join(map(str, result))}")