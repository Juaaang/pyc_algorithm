import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    num, change = input().split()
    N = len(num)
    change = int(change)
    set_num = set([num])
    tmp = set()
    for _ in range(change):
        while set_num:
            t = set_num.pop()
            t = list(t)
            for i in range(N):
                for j in range(i+1, N):
                    t[i], t[j] = t[j], t[i]
                    tmp.add(''.join(t))
                    t[i], t[j] = t[j], t[i]
        set_num, tmp = tmp, set_num


    print(f'#{tc}', max(map(int, set_num)))







