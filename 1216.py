import sys
sys.stdin = open('input.txt', 'r')



T = 10

def isPelindrome(s):
    s = s.rstrip()
    lenS = 0
    for _ in s:
        lenS += 1
    for idx in range(lenS//2):
        if s[idx] != s[lenS-1-idx]:
            return 0
    return 1

def my_max(lis):
    res = lis[0]
    for i in lis:
        if i > lis[0]:
            maxV = i
            if maxV > res:
                res = maxV
    return res


for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(100)]
    res = [0]*100
    length_2 = 100
    for i in range(100):
        length = 100
        new_str = ''
        for j in range(100):
            for k in range(j+1):
                if isPelindrome(arr[i][k:length+k]) == 1:
                    res[i] = length
                    break
            else:
                length -= 1
                if length == 0:
                    break
            new_str += arr[j][i]
        for l in range(i+1):
            if isPelindrome(new_str[l:length_2+l]) == 1:
                res[i] = length_2
                break
            else:
                length_2 -= 1
                if length_2 == 0:
                    break



    print(my_max(res))