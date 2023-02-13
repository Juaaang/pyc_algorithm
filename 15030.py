import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
    for i in string:
        if stack != [] and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{tc} {len(stack)}')