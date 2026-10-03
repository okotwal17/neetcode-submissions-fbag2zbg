# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0, True)
            leftHeight, leftbool = dfs(node.left)
            rightHeight, rightbool = dfs(node.right)
            if not leftbool or not rightbool:
                return (-1, False)
            return (1 + max(leftHeight, rightHeight), abs(leftHeight - rightHeight) <= 1)
        return dfs(root)[1]