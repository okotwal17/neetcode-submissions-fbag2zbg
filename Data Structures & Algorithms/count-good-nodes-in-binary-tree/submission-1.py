# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0
            elif node.val >= maxSoFar:
                print(maxSoFar, node.val, 1)
                maxSoFar = max(maxSoFar, node.val)
                return 1 + dfs(node.left, maxSoFar) + dfs(node.right, maxSoFar)
            else:
                print(maxSoFar, node.val, 2)
                maxSoFar = max(maxSoFar, node.val)
                return dfs(node.left, maxSoFar) + dfs(node.right, maxSoFar)
        return dfs(root, float("-inf"))