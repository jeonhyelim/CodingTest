n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1): #데이터 개수만큼 1~n
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: #현재 stack의 top 요소
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
        
print('\n'.join(result))