import sys
sys.stdin = open('input.txt', 'r')


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(x,y, bool):
    global ans
    ans = max(ans, visited[x][y])
    for d in range(4):
        newX = x + dr[d]
        newY = y + dc[d]
        if not (0 <= newX < N and 0 <= newY < N) or visited[newX][newY]:
            continue
        if info_map[newX][newY] < info_map[x][y]:
            visited[newX][newY] = visited[x][y] + 1
            dfs(newX, newY, bool)
            visited[newX][newY] = 0
        elif bool and info_map[newX][newY]-K < info_map[x][y]:
            tmp = info_map[newX][newY]
            info_map[newX][newY] = info_map[x][y] - 1
            visited[newX][newY] = visited[x][y] + 1
            dfs(newX,newY, False)
            visited[newX][newY] = 0
            info_map[newX][newY] = tmp



T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    info_map = [list(map(int, input().split())) for _ in range(N)]
    peak = 0
    for i in range(N):
        peak = max(peak, max(info_map[i]))

    ans = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if info_map[i][j] == peak:
                visited[i][j] = 1
                dfs(i,j, True)
                visited[i][j] = 0

    print(f'#{tc}', ans)