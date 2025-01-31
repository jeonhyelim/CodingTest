class Node:
    def __init__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
    
def pre_order(node): #루 왼 오
    print(node.data, end = '') #본인 출력
    if node.left_node != '.': #왼쪽이 공백 아니면
        pre_order(tree[node.left_node]) #왼쪽 호출
    if node.right_node != '.': #오른쪽이 공백 아니면 
        pre_order(tree[node.right_node]) #오른쪽 호출
    
def in_order(node): #왼 루 오 
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])
    
def post_order(node): #왼 오 루
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')
    

n = int(input())
tree = {}
for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()