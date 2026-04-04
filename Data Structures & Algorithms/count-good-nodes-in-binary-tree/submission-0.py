# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def traversal(curMax, cur):
            if not cur:
                return
            if cur.val>=curMax:
                self.count+=1
                curMax=cur.val
            traversal(curMax, cur.left)
            traversal(curMax, cur.right)
        traversal(root.val, root)
        return self.count
            