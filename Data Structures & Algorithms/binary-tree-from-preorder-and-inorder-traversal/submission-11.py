# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        valToIdx = {val : i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        def treeFromOrder(l, r):
            if l > r:
                return None
            node = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            node.left = treeFromOrder(l, valToIdx[node.val] - 1)
            node.right = treeFromOrder(valToIdx[node.val] + 1, r)
            return node
        return treeFromOrder(0, len(inorder) - 1)
        
