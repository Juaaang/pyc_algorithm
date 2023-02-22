import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
def tree(k):
    global num
    if k <= N:
        tree(k*2)
        arr[k] = num
        num += 1
        tree(k*2 + 1)

for tc in range(1,T+1):
    N = int(input())
    arr = [0] * (N+1)
    num = 1   # 값, k = 번호
    tree(1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')