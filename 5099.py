import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    i = 0
    curi = 0
    queue = []
    num = []
    while i < M+1:
        if len(queue) < N and i < M:
            queue.append(ci[i])
            num.append(i+1)
            i += 1

        else:
            queue[curi] = queue[curi] // 2
            if queue[curi] == 0:
                queue.pop(curi)
                num.pop(curi)
                if i < M:
                    queue.insert(curi, ci[i])
                    num.insert(curi,i+1)
                    i += 1
                    curi = (curi + 1) % len(num)
                else:
                    curi = curi % len(num)

                if len(num) == 1:
                    print(f'#{tc}', *num)
                    break
            else:
                curi = (curi +1) % len(num)









