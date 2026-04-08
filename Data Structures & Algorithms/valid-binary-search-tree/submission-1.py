# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        interval = [root.val, root.val]
        def dfs(interval, node):
            if not node:
                return True
            leftCondition = True if not node.left else False
            rightCondition = True if not node.right else False
            if node.left and node.left.val < interval[1]:
                leftCondition = True
                interval[1] = node.left.val

            if node.right and node.right.val > interval[0]:
                rightCondition = True
                interval[0] = node.right.val
        
            if leftCondition and rightCondition:
                return dfs(interval, node.left) and dfs(interval, node.right)
            else:
                return False
        return dfs(interval, root)