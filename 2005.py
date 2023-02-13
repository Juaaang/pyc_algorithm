import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if i == 0:
                arr[i].append(1)
            else:
                if j != 0 and j != i:
                    arr[i].append(arr[i-1][j] + arr[i-1][j-1])
                else:
                    arr[i].append(1)
    print(f'#{tc}')
    for k in range(N):
        print(*arr[k])


