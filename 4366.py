import sys
sys.stdin = open('input.txt', 'r')

def to_ten(arr, num):
    res = 0
    for i in range(len(arr)):
        if arr[i]:
            res += arr[i]*num**(len(arr)-1-i)
    return res

T = int(input())

for tc in range(1,T+1):
    binary = list(map(int, input()))
    trit = list(map(int, input()))
    N = len(binary)
    M = len(trit)
    for a in range(N):
        flag = False
        if binary[a] == 1:
            binary[a] = 0
            tmp = to_ten(binary, 2)
            gap = abs(to_ten(trit,3) -tmp)
            for num in range(M):
                if gap == (3**num) or gap == 2*(3**num):
                    ans = tmp
                    flag = True
                    break
            binary[a] = 1
        else:
            binary[a] = 1
            tmp = to_ten(binary, 2)
            gap = abs(to_ten(trit, 3) - tmp)
            for num in range(M):
                if gap == (3 ** num) or gap == 2 * (3 ** num):
                    ans = tmp
                    flag = True
                    break
            binary[a] = 0

        if flag:
            break
    print(f'#{tc}', ans)

