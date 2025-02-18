n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
B = list(map(int, input().split()))

for num in B:
    lt, rt = 0, n-1
    isExist = False
    
    while lt <= rt:
        mid = (lt + rt) // 2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
            
    if not isExist:
        print(0)