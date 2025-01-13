n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))
    
array.sort() #기본 정렬 라이브러리 - 오름차순

for i in array:
    print(i)