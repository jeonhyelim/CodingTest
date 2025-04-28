import sys
from collections import deque

# 컴퓨터의 수(N), 연결 쌍의 수(M) 입력
N = int(sys.stdin.readline())          # 컴퓨터(노드) 개수
M = int(sys.stdin.readline())          # 네트워크(간선) 개수

# 네트워크(그래프) 연결 정보 저장 (1번 ~ N번 컴퓨터, 인덱스 0은 사용 X)
net = [[] for _ in range(N + 1)]

# 네트워크 연결 정보 입력받기 (양방향이므로 양쪽 모두 추가)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

# 방문(감염) 기록 배열 (초기값: 모두 False)
visited = [False for _ in range(N + 1)]

# BFS(너비우선탐색)로 감염 시뮬레이션
def bfs():
    q = deque()             # BFS에 사용할 큐
    count = 0               # 1번을 제외한 감염된 컴퓨터 수

    q.append(1)             # 1번 컴퓨터부터 감염 시작
    visited[1] = True       # 1번 컴퓨터 감염 처리

    while q:
        cur = q.popleft()   # 현재 감염된 컴퓨터 하나 꺼냄

        # 현재 컴퓨터(cur)와 연결된 컴퓨터들 모두 확인
        for val in net[cur]:
            if not visited[val]:    # 아직 감염(방문)되지 않은 컴퓨터라면
                q.append(val)       # 큐에 추가(곧 감염시킴)
                visited[val] = True # 감염 처리
                count += 1          # 감염된 컴퓨터 수 1 증가

    print(count)    # 1번을 제외하고 감염된 컴퓨터의 총 수 출력

# BFS 함수 실행
bfs()