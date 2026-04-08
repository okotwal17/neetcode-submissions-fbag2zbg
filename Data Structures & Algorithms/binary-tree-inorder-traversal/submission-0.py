# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#left, cur, right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traversal(self, root):
            if not root:
                return 
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        
        inorder(root)
        return res
