import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort() #정렬
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))
res = []

def binary(array, target, n):
    start = 0
    end = n - 1
    key = "0"
    
    while start <= end:
        mid = (start + end)//2
        if target == array[mid]:
            key = "1"
            break
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return key
    
for target in m_list:
    res.append(binary(n_list, target, n))
print(" ".join(res)) #list를 문자열로 변환 후 출력