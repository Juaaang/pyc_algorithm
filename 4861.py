'''
N X N 배열
길이가 M인 회문
가로뿐만아니라 세로로도 찾아야함

i로 돌
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def isPelindrome(s):
    s = s.rstrip()
    lenS = 0
    for _ in s:
        lenS += 1
    for idx in range(lenS//2):
        if s[idx] != s[lenS-1-idx]:
            return 0
    return 1


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for j in range(N-M+1):
        for i in range(N):
            if isPelindrome(arr[i][j:M+j]) == 1:
                print(f'#{tc} {arr[i][j:M+j]}')

            new_str = ''
            for k in range(M):
                new_str += arr[j+k][i]

            if isPelindrome(new_str) == 1:
                print(f'#{tc} {new_str}')



