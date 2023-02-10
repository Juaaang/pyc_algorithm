import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    arr = [['0']*(len(str1)*4 + 1)  for _ in range(5)]
    for i in range(len(str1)):
        arr[2][i*4+2] = str1[i]
    for i in range(5):
        for j in range(len(str1)*4 + 1):
            if i % 2:
                if j % 2:
                    arr[i][j] = '#'
                else:
                    arr[i][j] = '.'
            elif i % 4 == 0:
                if j % 4 == 2:
                    arr[i][j] = '#'
                else:
                    arr[i][j] = '.'
            else:
                if j % 4 == 0:
                    arr[i][j] = '#'
                if j % 2:
                    arr[i][j] = '.'
        arr[i] = ''.join(str(s) for s in arr[i])
        print(arr[i], end='\n')