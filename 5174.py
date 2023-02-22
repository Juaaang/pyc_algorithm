import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def subtree(left):
    global cnt

    for i in range(2):
        if arr[i][left]:
            cnt += 1
            num = arr[i][left]
            subtree(num)

for tc in range(1,T+1):
    E, N = map(int, input().split())
    s = list(map(int, input().split()))
    arr = [[0]*(E+2) for _ in range(2)]
    for i in range(E):
        left = int(s[2*i])
        right = int(s[2*i+1])

        if arr[0][left] == 0:
            arr[0][left] = right
        else:
            arr[1][left] = right
    cnt = 1
    subtree(N)

    print(f'#{tc}', cnt)

