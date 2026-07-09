# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        def dfs(node, p, q):
            if not node:
                return -1
            print(p.val, q.val, node.val)
            if (p.val <= node.val and q.val >= node.val):
                return node
            elif p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)
            else:
                return dfs(node.right, p, q)
        return dfs(root, p, q)


