import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
delNode = int(input())

child = [[] for _ in range(n)] # 각 노드의 자식 노드 목록 저장

for idx in range(n):
    if parent[idx] == -1 or idx == delNode: # 루트, idx == delNode는 아예 트리에 추가하지 않음
        continue
    child[parent[idx]].append(idx) # 나머지 노드는 부모의 자식으로 추가 => child[x] x의 자식노드 리스트
    
def dfs(d): # 삭제처리 . d: 현재 방문한 노드 번호
    # 리프 노드인 경우(자식x)
    if child[d] == []:
        child[d].append(-1) # 이 서브트리의 모든 노드의 child를 다 [-1]로 바꿔버림 = 삭제
        return
    # 리프 노드가 아닌 경우(자식o)
    for c in child[d]:
        dfs(c) # 재귀

dfs(delNode) #delNode를 루트로 하는 서브트리 전부를 방문

# 리프 노드 개수 세기
ans = 0
for i in range(n):
    if child[i] == []: 
        ans += 1

print(ans) 
