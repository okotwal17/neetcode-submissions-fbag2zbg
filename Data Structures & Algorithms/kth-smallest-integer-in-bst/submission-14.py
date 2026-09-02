# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1
        self.i = 0
        def dfs(node):
            if not node:
                return
            if self.res != -1:
                return
            dfs(node.left)
            self.i += 1
            if self.i == k:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res