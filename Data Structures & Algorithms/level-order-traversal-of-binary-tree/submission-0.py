# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def bfs(root):
            q = deque()
            q.append(root)
            while len(q)!=0:
                curQLen = len(q)
                tempL = []
                for i in range(curQLen, 0, - 1):
                    curEle = q.popleft()
                    if not curEle:
                        continue
                    tempL.append(curEle.val)
                    q.append(curEle.left)
                    q.append(curEle.right)
                if len(tempL)>0:
                    self.res.append(tempL)
        bfs(root)
        return self.res
                

            