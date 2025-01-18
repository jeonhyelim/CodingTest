n = int(input())
arr = []

for _ in range(n):
    #1
    input_data = input().split(' ')
    arr.append( (int(input_data[0]),int(input_data[1])) )

    #2
    x, y = map(int, input().split(' '))
    arr.append((x,y))

arr = sorted(arr)
#key x, 기본 정렬 라이브러리

for i in arr:
    print(i[0],i[1])
