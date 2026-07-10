# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        res = [[root.val]]
        q.append(root)
        while q:
            print(q, res)
            n = len(q)
            #Add neighbors
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #Add to result
            level = []
            for node in q:
                level.append(node.val)
            if level:
                res.append(level)
        return res

