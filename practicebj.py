import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = map(int, input().split())
V = int(input())
cnt = 0
for i in arr:
    if i == V:
        cnt+=1
print(cnt)