N = int(input())

binaryTree = {}

# 딕셔너리에 루트 기준으로 왼쪽 값 오른쪽 값 초기화
for _ in range(N):
    r,l,r = input().split()
    binaryTree[r] = [l,r]

# 전위 순회
def preorder(root):
    if root != '.':
        print(root,end='')
        # 왼
        preorder(binaryTree[root][0])
        # 오
        preorder(binaryTree[root][1])

# 중위 순회
def inorder(root):
    if root != '.':
        # 왼
        inorder(binaryTree[root][0])
        print(root,end='')
        # 오
        inorder(binaryTree[root][1])

# 후위 순회
def postorder(root):
    if root != '.':
        # 왼
        postorder(binaryTree[root][0])
        # 오
        postorder(binaryTree[root][1])
        print(root,end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
