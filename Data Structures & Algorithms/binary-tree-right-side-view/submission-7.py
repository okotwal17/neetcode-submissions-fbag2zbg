# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        while len(q) != 0:
            curLen = len(q)

            for i in range(curLen):
                curNode = q.popleft()
                if i == 0:
                    res.append(curNode.val)
                if curNode.right:
                    q.append(curNode.right)
                if curNode.left:
                    q.append(curNode.left)
        return res
        
                


        