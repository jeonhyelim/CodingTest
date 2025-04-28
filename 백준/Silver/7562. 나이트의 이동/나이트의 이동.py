import sys
from collections import deque

input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    l = int(input())  # 체스판 한 변의 길이 (l x l)
    start_x, start_y = map(int, input().split())  # 시작 좌표 입력
    end_x, end_y = map(int, input().split())      # 도착 좌표 입력
    
    # 나이트가 이동할 수 있는 8가지 방향 (체스 규칙)
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # 방문 여부 체크하는 2차원 리스트 (l x l)
    visited = [[False]*l for _ in range(l)]
    
    # BFS를 위한 큐 생성, (x좌표, y좌표, 이동 횟수) 저장
    q = deque()
    q.append((start_x, start_y, 0))  # 시작 위치와 이동 횟수 0으로 큐에 삽입
    visited[start_x][start_y] = True # 시작 위치 방문 처리
    
    answer = 0   # 최소 이동 횟수 저장 변수
    found = False # 목표 지점에 도달했는지 여부
    
    # BFS
    while q and not found:   # 큐가 비어있지 않고, 아직 목적지 못 찾았으면 반복
        x, y, cnt = q.popleft()  # 현재 좌표와 이동 횟수 꺼내기
        
        # 목표 지점 도착시
        if x == end_x and y == end_y:
            answer = cnt    # 현재까지 이동 횟수가 정답
            found = True    # 목적지 도달 표시 후
            break           # 반복문 탈출 (최단 경로라 더 볼 필요 없음)
        
        # 8방향 모두 시도
        for dir in range(8):
            nx = x + dx[dir]  # 새로운 x좌표
            ny = y + dy[dir]  # 새로운 y좌표
            
            # 체스판 범위 내 & 방문하지 않은 곳만 큐에 추가
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True        # 방문 처리
                q.append((nx, ny, cnt + 1))  # 이동 횟수 +1 하여 큐에 저장
    
    print(answer)  # 최소 이동 횟수 출력