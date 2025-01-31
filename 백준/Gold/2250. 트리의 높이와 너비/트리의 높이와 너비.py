class Node:
    def __init__(self,number,left_node,right_node):
        self.parent = -1 #루트노드
        self.number = number
        self.left_node = left_node
        self.right_node = right_node
    
#중위
def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    #왼
    if node.left_node != -1:
        in_order(tree[node.left_node], level+1)
    #루트 - 데이터처리
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    #오
    if node.right_node != -1:
        in_order(tree[node.right_node], level+1)

n = int(input()) #노드 갯수
tree = {}
level_min = [n] #큰 값 노드의 개수
level_max = [0] 
root = -1
x = 1
level_depth = 1 #최대 깊이

#트리 초기화
for i in range(1,n+1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)
 
for _ in range(n):
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    #부모 정보 업데이트
    if left_node != -1: #존재함
        tree[left_node].parent = number
    if right_node != -1: #존재함
        tree[right_node].parent = number
    
for i in range(1, n+1):
    if tree[i].parent == -1: #부모 존재하지않음->루트노드
        root = i
        
in_order(tree[root], 1) #루트 노드에서 중위 순회 시작

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1): #모든 level에 대한 min max 차
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width
        
print(result_level, result_width)
