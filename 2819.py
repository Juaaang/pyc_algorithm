import sys
sys.stdin = open('input.txt', 'r')


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solve(x, y, curS):
    q = set()
    q.add((x, y, curS))
    while q:
        r, c, curS = q.pop()
        for d in range(4):
            newR = r + dr[d]
            newC = c + dc[d]
            if 0 <= newR < 4 and 0 <= newC < 4:
                if len(curS) == 6:
                    ans.add(curS+arr[newR][newC])
                else:
                    q.add((newR, newC, curS + arr[newR][newC]))
    return ans

T = int(input())
for tc in range(1,T+1):
    ans = set()
    arr = [list(map(str, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            solve(i, j, arr[i][j])

    print(f'#{tc}', len(ans))