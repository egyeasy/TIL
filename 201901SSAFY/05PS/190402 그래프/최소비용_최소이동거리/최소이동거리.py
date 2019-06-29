import sys

def dij(n):
    D = [99999999] * (n+1)      # 0번 부터의 거리
    D[0]  = 0                                  # 출발점
    for  x in adj[0]:
        D[x] = adj[0][x]                    # D 초기화
    V = [0] * (n+1)                 # 거리를 결정한 노드 기록
    V[0] = 1                            # 시작노드
    c = 0                                   # 처리된 노드 수
    while c<n:                              # 출발을 빼고 n개가 처리되면 됨
        minV = 999999                          #
        minIdx = 0
        for i in range(n+1):                        # 방문안한 노드 중 D가 최소인 노드 찾기
            if V[i] == 0 and D[i]<minV:
                minIdx = i
                minV = D[i]
        V[minIdx] = 1                       # D가 가장 작은 노드 처리 표시
        for x in adj[minIdx]:               # minIdx에 인접인 노드에 대해
            if D[x] > (D[minIdx]+adj[minIdx][x]):       # minIdx를 경유하는 비용이 더 작으면
                D[x] = D[minIdx]+adj[minIdx][x]            # D[x] 갱신
        c += 1
        
    return D[n]
    
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N, E= map(int, input().split())
    wt = {}
    adj = [{} for i in range(N+1)]

    for i in range(E):
        n1, n2, w =  map(int,input().split())
        adj[n1][n2] = w                 # adj[n1].update({n2:w})
    print('#{} {}'.format(tc, dij(N)))
