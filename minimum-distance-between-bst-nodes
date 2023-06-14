# This is the same as minimum-absolute-difference-in-bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverseTree(node: TreeNode, values: set):
    values.add(node.val)
    if node.right is not None:
        traverseTree(node.right, values)
    if node.left is not None:
        traverseTree(node.left, values)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = set()
        traverseTree(root, values)
        values = sorted(values)
        minDiff = max(values)
        print(values)
        for i in range(1, len(values)):
            delta = values[i] - values[i - 1]
            if delta < minDiff:
                minDiff = delta
        return minDiff