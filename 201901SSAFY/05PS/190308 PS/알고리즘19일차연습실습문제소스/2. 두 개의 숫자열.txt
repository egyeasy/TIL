import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    if len(B) > len(A) :
        for i in range(len(B) - len(A) + 1):
            sum = 0
            for j in range(len(A)):
                sum += (B[i + j] * A[j])
            if ans < sum : ans = sum
    elif len(B) < len(A):
        for i in range(len(A) - len(B) + 1):
            sum = 0
            for j in range(len(B)):
                sum += (A[i + j] * B[j])
            if ans < sum : ans = sum
    else:
        ans = 0
        for i in range(len(A)):
            ans += (A[i] * B[i])

    print("#%d"%tc, ans)



