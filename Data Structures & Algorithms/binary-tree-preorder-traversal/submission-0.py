# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#cur, left, right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def traversal(root):
            if not root:
                return 
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return res