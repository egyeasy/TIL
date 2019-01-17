import sys
sys.stdin = open("input.txt", "r")

def pyungtan(total_dt, alist, dt=0):
    new_list = sorted(alist)
    if total_dt == dt:
        return new_list[-1] - new_list[0]
    new_list[0] += 1
    new_list[-1] -= 1
    dt += 1
    return pyungtan(total_dt, new_list, dt)

for tc in range(1, 11):
    total_dt = int(input())
    alist = list(map(int, input().split()))
    print(f"#{tc} {pyungtan(total_dt, alist)}")