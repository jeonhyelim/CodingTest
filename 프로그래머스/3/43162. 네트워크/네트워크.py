def solution(n, computers):
    answer = 0
    visited = [False] * n  # 각 컴퓨터의 방문 여부를 기록

    
    def dfs(node):
        # 현재 노드를 방문 처리
        visited[node] = True
        
        # 현재 노드와 연결된 다른 모든 노드를 확인
        for neighbor in range(n):
            # 1. 연결되어 있고, 2. 아직 방문하지 않았다면
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                # 재귀적으로 방문
                dfs(neighbor)

                
    # 모든 컴퓨터를 순회
    for i in range(n):
        # 만약 아직 방문하지 않은 컴퓨터라면
        if not visited[i]:
            dfs(i)       # 그 컴퓨터와 연결된 모든 네트워크를 탐색
            answer += 1  # 탐색이 끝났다는 것은 하나의 네트워크를 찾았다는 의미
            
    return answer