import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N, string = map(int, input().split())
    stack = []
    for i in str(string):
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    result = ''.join(map(str, stack))
    result = result.lstrip('0')
    print(f'#{tc} {result}')