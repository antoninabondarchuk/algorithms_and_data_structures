# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    return is_mirror(root.left, root.right)


def is_mirror(left_node, right_node):
    if left_node is None and right_node is None:
        return True
    if left_node is None or right_node is None:
        return False
    return (left_node.val == right_node.val
            and is_mirror(left_node.left, right_node.right)
            and is_mirror(right_node.left, left_node.right))


if __name__ == '__main__':
    root = TreeNode(1)
    root_left = TreeNode(2)
    root_left.left = TreeNode(3)
    root.left = root_left

    root_right = TreeNode(2)
    root_right.right = TreeNode(3)
    root.right = root_right
    result1 = isSymmetric(root)
    print(result1)
