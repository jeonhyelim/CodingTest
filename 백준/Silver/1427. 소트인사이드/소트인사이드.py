array = input()

for i in range(9, -1, -1): # 9~0까지의 수 확인
    
    for j in array: #array 문자열의 각 문자 하나씩 꺼냄
        if int(j) == i:
            print(i, end = '')