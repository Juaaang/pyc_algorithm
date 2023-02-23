import sys
sys.stdin = open('input.txt', 'r')

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p>0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
    return
def parSum(last):
    res = 0
    while last > 1:
        p = last// 2
        res += heap[p]
        last = p
    return res
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    heap = [0]*(N+1)
    last = 0
    nums = list(map(int, input().split()))
    for num in nums:
        enq(num)
    print(f'#{tc}', parSum(last))