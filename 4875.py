'''
0 : 길  1: 벽 2: 출발점 3: 도착점

도착점에서 스타트해서 출발점을 찾으면 return 1
못찾으면 return 0
'''


import sys
sys.stdin = open('input.txt', 'r')

def dfs(row, col):
    ST = []
    visited = [[False]*N for _ in range(N)]

    ST.append((row,col))
    visited[row][col] = True
    while ST:
        row, col = ST.pop()
        for dr, dc in [(1, 0), (-1,0), (0,1), (0, -1)]:
            newR = row + dr
            newC = col + dc
            if 0 <= newR < N and 0 <= newC < N and maze_arr[newR][newC] != 1 and not visited[newR][newC]:
                if maze_arr[newR][newC] == 2:
                    return 1
                ST.append((newR, newC))
                visited[newR][newC] = True

    return 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze_arr = [list(map(int, input().strip())) for _ in range(N)]

    for row in range(N):
        if 3 in maze_arr[row]:
            col = maze_arr[row].index(3)
            break

    print(f'#{tc}', dfs(row,col))