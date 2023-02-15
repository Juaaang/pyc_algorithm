import sys
sys.stdin = open('input.txt', 'r')

def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot, tail = A[0], A[1:]

    leftside = [x for x in tail if x <= pivot]
    righside = [x for x in tail if x > pivot]

    return quick_sort(leftside) + [pivot] + quick_sort(righside)



A = list(map(int, input().split()))
sort_A = quick_sort(A)
print(sort_A[500000])