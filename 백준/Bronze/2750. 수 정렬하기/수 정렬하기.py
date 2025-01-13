n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

#1
array.sort() #기본 정렬 라이브러리 - 오름차순

#2
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)
