'''
집과 집사이의 거리 생각
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1, 2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    t = abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0  <= i <N and 0 <=j <N:
                            cnt += arr[i][j]
                # 운영비용보다 수익이 작지 않으면
                if ((k*k)+(k-1)*(k-1)) <= cnt*M:
                    mx = max(mx, cnt)
    return mx

def bfs(si,sj):
    q = []
    v = [[0]*N for _ in range(N)]
    old = 0
    mx = 0
    q.append((si,sj))
    v[si][sj]=1
    cnt = arr[si][sj]
    while q:
        ci, cj = q.pop(0)
        if old != v[ci][cj]: #k값이 달라진 경우
            old = v[ci][cj]
            if cost[v[ci][cj]] <=
        for di, dj in ((-1, 0), (1,0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] +1
                cnt += arr[ni][nj]


def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N):
            mx = max(mx, bfs(si,sj))
    return mx
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solve_loop()
    print(f'#{tc}', ans)
