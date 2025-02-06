n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]

for i in range(1,n): #두 번째 줄
    for j in range(i+1): #현재 줄의 원소 갯수
        if j == 0: #맨 왼쪽
            arr[i][j] += arr[i-1][j]
        elif j == i: #맨 오른쪽
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[n-1]))
            