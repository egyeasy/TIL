import sys
sys.stdin = open('1952.txt', 'r')

from collections import deque

def bfs(idx, visited):
    global global_min_price
    dq.append([idx, visited])
    while dq:
        idx, former_visited = dq.popleft()
        # idx 최대 처리
        if idx >= 12:
            continue
        # 해당 idx에 3달짜리 결제할 경우
        former_quarter_price = 0
        this_visited = former_visited[:]
        for i in range(3):
            if idx + i < 12 and this_visited[idx + i]:
                former_quarter_price += this_visited[idx + i][1]
        if quarter_price < former_quarter_price:
            this_visited[idx] = [3, quarter_price]
            for i in range(1, 3):
                if idx + i < 12:
                    this_visited[idx + i] = 0
            this_total = calculate_total(this_visited)
            if this_total < global_min_price:
                global_min_price = this_total
            dq.append([idx + 3, this_visited])
        # 해당 idx에 3달짜리 안 결제할 경우
        this_total = calculate_total(former_visited)
        if this_total < global_min_price:
            global_min_price = this_total
        dq.append([idx + 1, former_visited[:]])


def calculate_total(visited):
    total = 0
    for i in visited:
        if i:
            total += i[1]
    return total

T = int(input())
for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    visited = [0] * 12
    day_price, month_price, quarter_price, year_price = prices

    day_limit = month_price // day_price

    total_price = 0
    for month in range(12):
        if plan[month]:
            # day와 month 가격 비교해서 적용
            if plan[month] <= day_limit:
                # [가격제, 총 가격]
                visited[month] = [0, day_price * plan[month]]
            else:
                visited[month] = [1, month_price]
            total_price += visited[month][1]
    # print(plan)
    # print(prices)
    # print(f"#{tc} {visited}")
    # print("total price", total_price)
    # print()

    global_min_price = total_price
    start_month = 0
    for month in range(12):
        if plan[month]:
            dq = deque()
            bfs(month, visited)
            break

    if year_price < global_min_price:
        global_min_price = year_price

    print(f"#{tc} {global_min_price}")

