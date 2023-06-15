# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverseTree(node: TreeNode, level: int, values: dict):
    if level in values.keys():
        values[level].append(node.val)
    else:
        values[level] = [node.val]
    if node.left is not None:
        traverseTree(node.left, level + 1, values)
    if node.right is not None:
        traverseTree(node.right, level + 1, values)


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        vals = dict()
        level = 1
        traverseTree(root, level, vals)
        maxLevel = 1
        maxSum = None
        for key in vals.keys():
            currentSum = sum(vals[key])
            if maxSum is None:
                maxSum = currentSum
            elif currentSum > maxSum:
                maxLevel = key
                maxSum = currentSum
        return maxLevel