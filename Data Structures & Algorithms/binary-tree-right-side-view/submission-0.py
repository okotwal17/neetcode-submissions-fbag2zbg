# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def right(cur):
            if not cur:
                return 
            self.res.append(cur.val)
            if cur.right:
                right(cur.right)
            else:
                right(cur.left)
        right(root)
        return self.res