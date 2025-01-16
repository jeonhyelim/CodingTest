n = int(input())
array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]),input_data[1]))
    #첫번째 원소를 나이로, 나머지는 stable 먼저 들어온 순서를 지킴(오름차순)

array = sorted(array, key=lambda x: x[0]) #정렬- list.sort() or sorted(list)
#정렬기준 : 나이 x[0], 안정성 유지-> 동일 나이 데이터는 입력 순서 유지

for i in array:
    print(i[0], i[1])