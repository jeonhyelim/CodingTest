from collections import deque

n,m = map(int, input().split()) #섬, 다리
adj = [[] for _ in range(n+1)] #인접 리스트를 이용한 그래프 초기화

def bfs(c):
    queue = deque([start_node]) #BFS 탐색을 위한 큐 초기화
    visited = [False] * (n+1) #방문 체크 배열
    visited[start_node] = True #시작점을 방문표시
    while queue:
        x = queue.popleft() #현재노드
        for y, weight in adj[x]: #연결된 노드(y)와 다리의 중량 제한 체크
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

#양방향 그래프로 다리 정보 저장
for _ in range(m):
    x, y, weight = map(int,input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight) #다리 중 최소 중량
    end = max(end, weight) #다리 중 최대 중량
    
start_node, end_node = map(int, input().split())

result = start #최소중량으로 초기화
#이진탐색
while(start <= end):
    mid = (start + end) // 2 #중량의 중간값
    if bfs(mid): #이동 가능 -> 중량 증가
        result = mid
        start = mid + 1
    else: #이동 불가 -> 중량 감소
        end = mid - 1
        
print(result)
        
