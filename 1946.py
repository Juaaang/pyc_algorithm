import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    ans = ''
    for i in range(N):
        ans += arr[i][0] * int(arr[i][1])
    print(f'#{tc}')
    for num in ans:
        if len(ans) > 10:
            print(ans[:10], end='\n')
            ans = ans[10:]
        else:
            print(ans)
            break

