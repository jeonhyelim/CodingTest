#1.DP Dynamic Programming 동적 계획법 - BottomUp 풀이(for)
x = int(input())
d = [0] * (x+1) #d[i]; i를 1로 만드는 데 필요한 최소 연산횟수 저장 배열

for i in range(2, x+1): #2~x
    d[i] = d[i-1] + 1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)

print(d[x])

#2.DP - Topdown 풀이 (재귀)


#3.BFS
