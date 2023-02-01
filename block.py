blocks = [7, 4, 2, 0, 0, 6, 0, 7, 0]
N = len(blocks)
curMaxV = 0
for i in range(N):  # N의 길이 만큼 i가 돌면서
    cnt = 0
    for j in range(i+1, N):   # j를 i+1 부터 끝까지 돌리면서
        if blocks[i] > blocks[j]:   # 만약 block 의 i 가 j 보다 크면
            cnt += 1   # 카운트

    if curMaxV < cnt:       # 한 단위가 돌고 cnt 의 값을 curMaxV 와 비교
        curMaxV = cnt

print(f'최대값 : {curMaxV}')