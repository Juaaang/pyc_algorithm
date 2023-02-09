import sys
sys.stdin = open('input.txt', 'r')

T = 10

def isPelindrome(s):
    s = s.rstrip()
    lenS = len(s)
    for idx in range(lenS//2):
        if s[idx] != s[lenS-1-idx]:
            return 0
    return 1
for tc in range(1, 11):
    length = int(input())
    board = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-length+1):
            if isPelindrome(board[i][j:j+length]) == 1:
                cnt += 1

            new_str = ''
            for k in range(length):
                new_str += board[j + k][i]

            if isPelindrome(new_str) == 1:
                cnt += 1
    print(f'#{tc} {cnt}')