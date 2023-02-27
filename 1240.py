import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = {'0':'0001101', '1':'0011001', '2':'0010011',
     '3':'0111101', '4':'0100011', '5':'0110001',
     '6':'0101111', '7':'0111011', '8':'0110111',
     '9':'0001011'}
def decoding():
    ST = []
    k=0
    while True:
        if len(ST) == 7:
            if ''.join(map(str, ST)) in d.values() and board[row][k] != '1':
                ST.extend(board[row][k:k+49])
                res = ''.join(map(str, ST))
                return res
            else:
                ST.pop(0)
        else:
            ST.append(board[row][k])
            k+=1

for tc in range(1,T+1):
    N, M = map(int, input().split())
    board = [list(map(str, input())) for _ in range(N)]
    for i in range(N):
        if len(set(board[i][:])) == 2:
            row = i
            break
    a = decoding()
    ans = ''
    bb = {v:k for k,v in d.items()}
    for i in range(0, 56, 7):
        ans += bb.get(a[i:i+7])
    sumT = 0
    for j in range(len(ans)):
        if j % 2:
            sumT += int(ans[j])
        else:
            sumT += int(ans[j])*3

    if sumT %10 :
        print(f'#{tc} 0')
    else:
        result = 0
        for i in ans:
            result += int(i)
        print(f'#{tc}', result)
