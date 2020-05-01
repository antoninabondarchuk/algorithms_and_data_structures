# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if (p.val is None) and (q.val is None):
        return True
    elif p and q:
        return(p.val == q.val
               and isSameTree(p.left, q.left)
               and isSameTree(p.right, q.right))
    return False


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)

    result1 = isSameTree(p, q)
    print(result1)
