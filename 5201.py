import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(key=lambda x : -x)
    t.sort(key=lambda x : -x)
    ans = 0
    if len(t) >= len(w):
        k = 0
        for i in range(len(w)):
            for j in range(k, len(t)):
                if w[i] <= t[j]:
                    ans += w[i]
                    k += 1
                    break
        print(f'#{tc}', ans)
    else:
        k = 0
        for i in range(len(t)):
            for j in range(k, len(w)):
                if w[j] <= t[i]:
                    ans += w[j]
                    k += 1
                    break
        print(f'#{tc}', ans)