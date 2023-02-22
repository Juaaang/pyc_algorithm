import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def bfs(si, sj):
    Q = []
    visited = [[-1]*N for _ in range(N)]
    Q.append((si,sj))
    visited[si][sj] = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cnt = 1
    while Q:
        ci, cj = Q.pop(0)
        for d in range(4):
            newR = ci +dr[d]
            newC = cj +dc[d]
            if 0<= newR < N and 0<= newC < N and visited[newR][newC] == -1 and arr[newR][newC] == arr[ci][cj]+1:
                cnt += 1
                visited[newR][newC] = 0
                Q.append((newR,newC))

    return cnt


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxCnt = 0
    minPoint = N**2
    for i in range(N):
        for j in range(N):
            point = arr[i][j]
            count = bfs(i,j)

            if count > maxCnt:
                maxCnt = count
                minPoint = point

            elif count == maxCnt:
                if point < minPoint:
                    minPoint = point

    print(f'#{tc} {minPoint} {maxCnt}')

