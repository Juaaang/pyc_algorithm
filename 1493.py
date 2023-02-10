'''
point = 10000일때까지 좌표를 찾아보면서
arr범위를 찾음
'''

import sys
sys.stdin = open('input.txt', 'r')

def new_method1(a, b):
    x = y = point = 1
    while True:
        if x == a and y == b:
            return point
        if y == 1:
            y += x
            x = 1
        else:
            y -= 1
            x += 1
        point+= 1
def new_method2(num):
    x = y = point = 1
    while True:
        if point == num:
            return x, y
        if y == 1:
            y += x
            x = 1
        else:
            y -= 1
            x += 1
        point += 1


T = int(input())
for tc in range(1,T+1):
    p, q = map(int, input().split())
    p = new_method2(p)
    q = new_method2(q)
    r = p[0]+q[0], p[1]+q[1]
    print(f'#{tc} {new_method1(r[0], r[1])}')