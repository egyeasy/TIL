import sys
sys.stdin = open('4008.txt', 'r')


def backtrack(arr, k, operators):
    global global_max, global_min
    if k == M_oper:
        cal_value = calculate(arr)
        if cal_value > global_max:
            global_max = cal_value
        if cal_value < global_min:
            global_min = cal_value
    else:
        k += 1
        for i in range(4):
            if operators[i]:
                new_operators = operators[:]
                new_operators[i] -= 1
                arr[k - 1] = i
                backtrack(arr, k, new_operators)
                arr[k - 1] = -1


def calculate(operators):
    result = nums[0]
    for i in range(M_oper):
        # print("#", i, "curr", result, "calcul", arr[i], "num", nums[i + 1])
        if arr[i] == 0:
            result += nums[i + 1]
        elif arr[i] == 1:
            result -= nums[i + 1]
        elif arr[i] == 2:
            result *= nums[i + 1]
        else:
            result = int(result / nums[i + 1])
    return result


T = int(input())
for tc in range(1, T + 1):
    N_num = int(input())
    M_oper = N_num - 1
    operators = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    arr = [-1] * (N_num - 1)
    global_min = 100000001
    global_max = -100000001
    backtrack(arr, 0, operators)
    print(f"#{tc} {global_max - global_min}")