import sys
sys.stdin = open('input.txt', 'r')



T = 10

def pel_chk(x, y, dir, max_len):
    string = ''
    if dir == 0:
        for k in range(100-y):
            string += board[x][y+k]
            if len(string) < max_len:
                continue
            if string == string[::-1]:
                max_len = len(string)
    else:
        for k in range(100 - x):
            string += board[x + k][y]
            if len(string) < max_len:
                continue
            if string == string[::-1]:
                max_len = len(string)
    return max_len

for tc in range(1, 11):
    N = input()
    board = [input() for _ in range(100)]
    max_len = 0
    for i in range(100):
        for j in range(100):
            max_len = max(pel_chk(i, j, 0, max_len), pel_chk(i, j, 1, max_len))

    print(f'#{tc} {max_len}')