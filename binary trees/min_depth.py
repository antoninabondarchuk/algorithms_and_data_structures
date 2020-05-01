# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = minDepth(root.left)
    right_depth = minDepth(root.right)
    if left_depth != 0 and right_depth != 0:
        return 1 + min(right_depth, left_depth)
    return 1 + right_depth + left_depth


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    result1 = minDepth(root)
    print(result1)
