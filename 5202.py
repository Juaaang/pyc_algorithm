import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lis = []
    for i in range(N):
        s, e = map(int, input().split())
        lis.append([s, e])

    lis.sort(key=lambda x: [x[1], x[0]])

    ans = 1
    end_t = lis[0][1]
    for j in range(1, N):
        if lis[j][0] >= end_t:
            ans += 1
            end_t = lis[j][1]

    print(f'#{tc}', ans)