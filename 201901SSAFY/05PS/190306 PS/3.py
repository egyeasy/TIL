import sys
sys.stdin = open('3.txt', 'r')

def judge(num):
    word = str(num)
    length = len(word)
    judge = True
    for i in range(1, length):
        if word[i] < word[i - 1]:
            judge = False
            break
    return judge

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    max_result = 0
    for i in range(N - 1):
        a = nums[i]
        # for j in range(i + 1, N) 이라고 하면 중복 피할 수 있음
        for j in range(i + 1, N):
            if not i == j:
                b = nums[j]
                result = a * b
                if judge(result) and result > max_result:
                    max_result = result
    if max_result:
        print("#{}".format(tc), max_result)
    else:
        print("#{} -1".format(tc))

