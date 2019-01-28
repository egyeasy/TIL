"""
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.


> 입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

> 출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
*****
 ****
  ***
   **
    *

"""

n = int(input())
for i in range(n, 0, -1):
    m = n-i
    print(" "*m+"*"*(i))


# 생각
# 1. c++로 해본 것들이라 아주 쉽게 생각해내서 짤 수 있다.