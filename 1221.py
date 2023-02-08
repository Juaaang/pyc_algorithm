import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    Num, N = input().split()
    nums = input().split()
    nums_to_idx = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    preV = nums[0]
    for i in range(len(nums)-1, 0 , -1):
        for j in range(i):
            if nums_to_idx.index(nums[j]) > nums_to_idx.index(nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(Num)
    print(*nums)