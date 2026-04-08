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
        leftCondition = False
        rightCondition = False
        if root.left and root.left.val < root.val or not root.left:
            leftCondition = True
        if root.right and root.right.val > root.val or not root.right:
            rightCondition = True
        
        if leftCondition and rightCondition:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
