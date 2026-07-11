# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, count = [0], [k]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if count[0] == 0:
                return
            count[0] -= 1
            if count[0] == 0:
                res[0] = node.val
                return
            dfs(node.right)
        dfs(root)
        return res[0]
