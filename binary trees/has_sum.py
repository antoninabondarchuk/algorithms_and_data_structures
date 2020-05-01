# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right and sum == root.val:
        return True
    sum -= root.val
    left = hasPathSum(root.left, sum)
    right = hasPathSum(root.right, sum)
    return left or right


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(1)

    result1 = hasPathSum(root, 22)
    print(result1)

    root2 = TreeNode(1)
    result2 = hasPathSum(root2, 0)
    print(result2)
