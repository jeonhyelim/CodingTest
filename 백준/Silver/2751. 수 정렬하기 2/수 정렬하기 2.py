def merge_sort(array):
    if len(array) <= 1: #이미 정렬된 상태
        return array
    
    mid = len(array) // 2 #배열을 절반으로 나눔
    left = merge_sort(array[:mid]) #왼쪽 부분 배열에 대해 재귀 호출
    right = merge_sort(array[mid:]) #오른쪽 부분 배열에 대해 재귀 호출
    
    i, j, k = 0,0,0 #왼쪽, 오른쪽, 원본 배열 인덱스 
    while i < len(left) and j < len(right):
        if left[i] < right[j]: #왼쪽 배열의 요소가 더 작으면
            array[k] = left[i] #원본 배열에 추가
            i += 1
        else: #오른쪽 배열의 요소가 더 작거나 같으면
            array[k] = right[j] 
            j += 1
        k += 1
        
    if i == len(left): #왼쪽 배열 먼저 끝났을때
        while j < len(right): #오른쪽 배열의 나머지 요소 추가
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right): #오른쪽 배열이 먼저 끝난 경우
        while i < len(left): #왼쪽 배열의 나머지 요소 추가
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input())) #리스트 array 생성


#1
array = merge_sort(array) #병합 정렬 수행
#2
array = sorted(array)


for data in array: #정렬된 배열 출력
    print(data)

