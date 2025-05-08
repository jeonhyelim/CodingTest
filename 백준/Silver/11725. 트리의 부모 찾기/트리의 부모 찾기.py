import sys
sys.setrecursionlimit(10**6) # 재귀 오류 -> 한도 늘림

N = int(sys.stdin.readline()) # 노드 개수
 
# 그래프 생성
graph = [[] for i in range(N+1)] # 1~N
for i in range(N-1): # 양방향 연결 인접리스트에 저장
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
# 방문 여부, 각 인덱스를 노드로 사용해 방문했으면 0을 지우고, 부모 노드를 저장
visited = [0]*(N+1) 
 
# dfs - 재귀
def dfs(node):
    for i in graph[node]: # 해당 노드에 인접한 노드 중에서
        if visited[i] == 0: # 방문한 적이 없다면
            visited[i] = node # 해당 노드를 부모 노드로 저장
            dfs(i) # 그 다음 깊이 탐색
 
dfs(1) # 루트노드부터 시작
 
for x in range(2, N+1):
    print(visited[x]) # 각 인덱스(노드)에 저장된 부모 노드 가져오기

