nums = [55, 7, 78, 12, 42]          # 오름차순
N = len(nums)

'''
for i in range(N-1, 0, -1):   # range(start, stop, step) -> N-1부터 0까지 -1씩 반복
    for j in range(i):            # 첫 i값이 4이므로 4전까지 j를 돌림 (j는 0, 1, 2, 3)
        if nums[j] > nums[j + 1]:     # 가장 큰 값인 j = 3 일때 nums 의 끝값인 3, 4 번 인덱스가 비교됨
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(*nums)
'''

# 왼쪽부터 채우는 방법으로 진행
for i in range(0, N):
    for j in range(i, 0, -1):
        if nums[j-1] < nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]

print(*nums)