'''
bfs틀 4방향/범위내, 미방문, 조건 -> Q삽입+
내가 이동할 방향 파이프에 내쪽 연결이 있으면
P = [[], [0, 1, 2, 3], [0, 1],  ....]
for dr in p[arr[ci][cj]]: -> 내 연결방향
    ni, nj <- 계산
    if opp[dr] in p[arr[ni][nj]]:       opp= {0:1,1:0,2:3,3:2}
        q 삽입, v[n] <- v[c] + 1, cnt+= 1

    *종료조건: L
        꺼냇는데 == L
        v[ci][cj]

N : 세로크기
M : 가로크기
R, C : 맨홀뚜껑이 위치한 장소의 세로,가로 위치
L : 탈출 후 소요된 시간

연결되어있으면 이동가능
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(N,M,R,C,L)
    print(arr)