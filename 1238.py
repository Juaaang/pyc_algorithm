import sys
sys.stdin = open('input.txt', 'r')

T = 10

def bfs(S):
    Q = [S]
    visited[S] = 0
    while Q:
        num = Q.pop(0)
        for i in Gr[num]:
            if visited[i] == 0:
                visited[i] = visited[num] + 1
                Q.append(i)

for tc in range(1, T+1):
    length, start = map(int, input().split())
    arr = list(map(int, input().split()))
    Gr = [[] for _ in range(101)]
    visited = [0]*101
    for i in range(0, len(arr), 2):
        Gr[arr[i]].append(arr[i+1])
    bfs(start)
    a = max(visited)
    max_num = 0
    for i in range(len(Gr)):
        if visited[i] == a and max_num < i:
            max_num = i
    print(f'#{tc}', max_num)

# bfs(s)
# q, v 필요 flag 생성
# q 초기데이터(들) 삽입, v 표시, 필요처리
# while Q:
#    q 한개 꺼냄 ( 정답처리 )
#    if v[ans] < v[c] or (v[ans] == v[c] and ans< c):
#       ans <- c
#    4/8 방향, 미방문 (조건 맞으면)
#          q 삽입, v표시