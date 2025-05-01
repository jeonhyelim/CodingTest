def build_graph(n, wires): #그래프를 인접리스트로 생성
    graph = [[] for _ in range(n+1)] #1~n까지의 노드를 담는 리스트
    for a,b in wires: # a,b에 연결된 노드목록 양방향 연결
        graph[a].append(b)
        graph[b].append(a)
    return graph

def dfs(node, parent, graph): # 한 쪽 서브트리의 노드개수 구하기 위한 함수(현재 탐색할 노드, 방금 방문한 이전 노드)
    cnt = 1 # 자기 자신 포함
    for child in graph[node]: # 현재 노드에 연결된 모든 child에 대해
        if child != parent: #parent가 아닌 경우
            cnt += dfs(child,node,graph) #재귀적으로 dfs 수행 -> 서브트리의 노드 수 누적 
    return cnt # 해당 노드를 루트로 했을 때 전체 노드수

def solution(n,wires):
    graph = build_graph(n,wires) #전체 트리를 그래프로 만든 후 저장
    min_diff = float("inf") #두전력망 노드 수 차이의 최솟값을 저장할 변수 
    
    for a,b in wires:
        graph[a].remove(b) #간선 하나씩 끊으며 실험
        graph[b].remove(a)
        
        cnt_a = dfs(a,b,graph)
        cnt_b = n - cnt_a
        
        min_diff = min(min_diff, abs(cnt_a - cnt_b)) #두 차이 절댓값 계산
        
        graph[a].append(b) #복원 -> 반복
        graph[b].append(a)
        
    return min_diff
        
        