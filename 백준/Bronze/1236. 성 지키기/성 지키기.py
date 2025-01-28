n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

#경비원 x: 0 / 경비원 o: 1
row = [0] * n 
column = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0 #경비원이 없는 행의 개수
for i in range(n):
    if row[i] == 0:
        row_count += 1

column_count = 0 #경비원이 없는 열의 개수
for j in range(m):
    if column[j] == 0:
        column_count += 1
        
print(max(row_count,column_count))