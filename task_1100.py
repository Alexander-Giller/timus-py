n: int = int(input())


class TreeNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.val = key
        self.second_val = value


def insert(root, key, value):
    if root is None:
        return TreeNode(key, value)

    if key <= root.val:
        root.right = insert(root.right, key, value)
    else:
        root.left = insert(root.left, key, value)

    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(str(root.second_val) + " " + str(root.val))
        inorder_traversal(root.right)


root = None
for i in range(n):
    input_line = input().split(' ')
    team_id: int = int(input_line[0])
    count: int = int(input_line[1])
    root = insert(root, count, team_id)

inorder_traversal(root)
