# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [-1]
        self.i = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.i += 1
            if self.i == k and res[0] == -1:
                res[0] = node.val
            dfs(node.right)
        dfs(root)
        return res[0]
        