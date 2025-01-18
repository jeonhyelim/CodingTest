import sys

n = int(sys.stdin.readline())
array = [0] * 10001 #크기가 10001인 배열 각 0으로 초기화 

for i in range(n):
    data = int(sys.stdin.readline()) #시간초과 방지
    array[data] += 1 #인덱스에 해당하는 배열 값 증가시킴

for i in range(10001): #0~10000
    if array[i] != 0: #해당 숫자 등장
        for j in range(array[i]): #계수정렬 처리
            print(i)