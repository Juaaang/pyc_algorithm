import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
fi = [0]*31
fi[0] = 0
fi[1] = 1
fi[2] = 3
def func(n):
    if n>= 3 and fi[n] == 0:
        t1 = func(n-1)
        t2 = 2*func(n-2)
        fi[n] = t1 + t2
    return fi[n]

for tc in range(1, T+1):
    N = int(input())
    n = N//10
    print(f'#{tc} {func(n)}')