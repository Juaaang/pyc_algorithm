import sys
sys.stdin = open('input.txt', 'r')

T = 10
def inOrder(rootIdx):
    global res
    if rootIdx < len(word_lis):
        inOrder(rootIdx*2)
        res.append(word_lis[rootIdx])
        inOrder(rootIdx*2+1)

for tc in range(1, T+1):
    N = int(input())
    word_lis = [0]*(N+1)
    for i in range(1, N+1):
        num, *s = list(input().split())
        word_lis[i] = s[0]
    res = []
    inOrder(1)
    print(f'#{tc}', ''.join(map(str, res)))