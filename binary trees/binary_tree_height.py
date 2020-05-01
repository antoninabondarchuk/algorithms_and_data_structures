# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root: TreeNode) -> bool:

    def check(root):
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != -1


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(-10)
    root.left.left = TreeNode(-20)
    root.left.left.left = TreeNode(-100)
    result1 = isBalanced(root)
    print(result1)
