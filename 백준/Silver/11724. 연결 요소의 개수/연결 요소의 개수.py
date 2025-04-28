import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())   # N: 정점 개수, M: 간선 개수

# 인접 리스트 그래프 만들기 (정점 번호는 1번부터 N번까지)
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력받아 양방향 연결
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)     # u와 v 연결
    graph[v].append(u)     # v와 u 연결 (무방향)

# 방문 기록 배열 (정점 번호 1~N 사용, 0은 미사용)
visited = [False] * (N + 1)

# BFS 함수 정의: start에서 시작해 연결된 모든 노드 방문 처리
def bfs(start):
    q = deque([start])         # 시작점을 큐에 넣음
    visited[start] = True      # 시작점 방문 표시

    while q:                   # 큐가 빌 때까지 반복
        v = q.popleft()        # 현재 노드 꺼내기

        # 현재 노드 v와 연결된 모든 노드 순회
        for nv in graph[v]:
            if not visited[nv]:      # 아직 방문하지 않은 노드라면
                visited[nv] = True   # 방문 처리
                q.append(nv)         # 큐에 추가

# 연결 요소 개수 세기
count = 0
for i in range(1, N + 1):          # 모든 정점 1~N 순회
    if not visited[i]:             # 아직 방문하지 않은 노드라면 (=새로운 그룹 발견)
        bfs(i)                     # 그 노드를 시작점으로 BFS 탐색
        count += 1                 # 탐색이 끝나면 연결 요소 개수 +1

print(count)                       # 전체 연결 요소 개수 출력