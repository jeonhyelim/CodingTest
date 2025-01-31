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
x = int(input())
dp = {1:0} #딕셔너리로 초기화. 1일때 연산횟수 0 가짐

def rec(n): #재귀적으로 dp 딕셔너리 채워나감
    if n in dp.keys(): #종료조건; 입력받은 n이 dp딕셔너리의 key에 존재하는 경우
        return dp[n]
        
    if (n%3 == 0) and (n%2 == 0):
        dp[n] = min(rec(n//3)+1, rec(n//2)+1)
    elif n%3 == 0:
        dp[n] = min(rec(n//3)+1, rec(n-1)+1)
    elif n%2 == 0:
        dp[n] = min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n] = rec(n-1) + 1
    return dp[n]
    
print(rec(x))


#3.BFS - 최단거리
from collections import deque

x = int(input())
Q = deque([x]) #큐 초기화 ; 시작점:x
visited = [0]*(x+1) #연산 횟수 저장(방문한 배열)

while Q:
    c = Q.popleft() #현재 숫자
    
    if c == 1:
        break
        
    if c%3 == 0 and visited[c//3] == 0:
        Q.append(c//3)
        visited[c//3] = visited[c]+1
    if c%2 == 0 and visited[c//2] == 0:
        Q.append(c//2)
        visited[c//2] = visited[c]+1
    if visited[c-1] == 0:
        Q.append(c-1)
        visited[c-1] = visited[c]+1
        
print(visited[1])

