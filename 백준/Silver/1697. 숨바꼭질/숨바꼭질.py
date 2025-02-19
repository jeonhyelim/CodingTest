from collections import deque

def bfs(n,k):
    max_num = 100000
    visited = [0] * (max_num + 1)

    q = deque([n]) #큐 초기값 설정
    while q:
        x = q.popleft() #현 위치 꺼내기
        
        if x == k: #목적지 k에 도착 -> 최단 거리 출력 , 종료
            return visited[x]
            
        for j in (x-1, x+1, x*2):
            if 0 <= j <= max_num and visited[j] == 0:
                visited[j] = visited[x] + 1 #이동한 위치의 최단 거리 갱신
                q.append(j) #이동 위치 큐에 추가, 다음 탐색

n, k = map(int, input().split())

print(bfs(n,k))