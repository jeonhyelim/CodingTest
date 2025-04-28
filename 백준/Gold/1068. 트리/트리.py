import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
delNode = int(input())

child = [[] for _ in range(n)] # 각 노드의 자식 노드 목록 저장

for idx in range(n):
    if parent[idx] == -1 or idx == delNode: # 부모가 -1이면 루트, idx == delNode이면, 삭제될 노드는 아예 트리에 추가하지 않음
        continue
    child[parent[idx]].append(idx) # 나머지 노드는 부모의 자식으로 추가
    
def dfs(d): # 삭제처리 delNode를 루트로 하는 서브트리 전부를 방문
    # 리프 노드인 경우
    if child[d] == []:
        child[d].append(-1) # 이 서브트리의 모든 노드의 child를 다 [-1]로 바꿔버림 
        return
    # 리프 노드가 아닌 경우
    for c in child[d]:
        dfs(c)

dfs(delNode)

ans = 0
for i in range(n):
    if child[i] == []: # 리프 노드 개수 세기
        ans += 1

print(ans) 