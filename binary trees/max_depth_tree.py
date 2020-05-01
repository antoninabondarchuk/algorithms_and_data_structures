class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == '__main__':
    root = TreeNode(3)
    root_l = TreeNode(9)
    root_r = TreeNode(20)
    root_r.left = TreeNode(15)
    root_r.right = TreeNode(7)
    root.left = root_l
    root.right = root_r
    result1 = maxDepth(root)
    print(result1)
