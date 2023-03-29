import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    station, *charge = map(int, input().split() + [0])
    charge = charge[::-1]
    i = 0
    cnt = 0
    while i < station-1:
        for j in range(station-1, i, -1):
            if j-i <= charge[j]:
                i = j
                if i == station-1:
                    break
                else:
                    cnt += 1
                    break
    print(f'#{tc}', cnt)