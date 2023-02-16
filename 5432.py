import sys
sys.stdin = open('input.txt', 'r')

T= int(input())

def stack(s):
    ST = []
    for i in s:
        if i == '(':
            ST.append(i)
        else:
            if ST[-1] == '(':
                cnt += 1


for tc in range(1,T+1):
    s = input()
