# 3 X 4  2차원 배열 입력
'''
M = 4 , N= 3
4
3
12 34 32
34 45 32
12 34 32
34 45 32
'''


# M = int(input())
# N = int(input())
# L = [list(map(int, input().split())) for _ in range(M)]
# print(L)
# maxV = 0
# for row in range(0, M):
#     sumV = 0
#     for col in range(0, N):
#         sumV += L[row][col]
#     print(sumV)
#     if maxV < sumV:
#         maxV = sumV

#재귀
# def factorial(n):
#     if n == 1:
#         return 1
#     t = n * factorial(n-1)
#     return t
#
# print(factorial(5))

# memoization
# fi = [0]*100
# fi[0] = 0
# fi[1] = 1
# def fibo(n):
#     if n>= 2 and fi[n] == 0:
#         t1 = fibo(n-1)
#         t2 = fibo(n-2)
#         fi[n] = t1 + t2
#
#     return fi[n]
#
# print(fibo(10))

V = 7+1 #(0번은 안쓸거임)
# E =
S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
S = list(map(int, S.split()))
G = [[0,0,0,0,0,0,0,0],
     [0,0,1,1,0,0,0,0],
     [0,1,0,0,1,1,0,0],
     [0,1,0,0,0,0,0,1],
     [0,0,1,0,0,0,1,0],
     [0,0,1,0,0,0,1,0],
     [0,0,0,0,1,1,0,1],
     [0,0,0,1,0,0,1,0],
     ]

# 인접행렬
def dfs(v):
    ST = []
    visited = [False] * V
    ST.append(v)
    visited[v] = True
    while ST:
        v = ST.pop()
        print(v)
        for w in range(V):
            if G[v][w] and not visited[w]:
                ST.append(w)
                visited[w] = True
dfs(1)


#인접그래프
# G = [[0]*V for _ in range(V)]
# for idx in range(0, len(S), 2):
#     v1 = S[idx]
#     v2 = S[idx+1]
#     G[v1][v2] = 1
#     G[v2][v1] = 1
# print(G)

# DFS (깊이우선탐색)

# 인접 리스트
# G = [[] for _ in range(V)]
# for idx in range(0, len(S), 2):
#     v1 = S[idx]
#     v2 = S[idx+1]
#     G[v1].append(v2)
#     G[v2].append(v1)


# DFS (깊이우선탐색)
G = [[], [2,3], [1,4,5], [1,7], [2,6], [2,6], [4,5,7], [3,6]]
# def dfs(v):
#     ST = []
#     visited = [False] * V
#
#     ST.append(v)
#     visited[v] = True
#     print(v) # 시작점
#     while ST:
#         for w in G[v]:
#             if not visited[w]:
#                 visited[w] = True # 방문점
#                 print(w)
#                 ST.append(v)
#                 v = w
#                 break
#         else:
#             v = ST.pop()
# dfs(1)

# def dfs(v):
#     ST = []
#     visited = [False] * V
#
#     ST.append(v)
#     visited[v] = True
#     while ST:
#         v = ST.pop()
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#                 visited[w] = True

# def dfsr(v):   # 4개로 연결된 그래프라고 생각되기 때문에 별로 안좋음 (메모리 많이먹음)
#     print(v)
#     visited[v] = True
#     for w in G[v]:
#         if not visited[w]:
#             dfsr(w)
# dfsr(1)