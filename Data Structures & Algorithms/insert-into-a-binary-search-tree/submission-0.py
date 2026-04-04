# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val, None, None)
        if not root:
            return node
        def helper(curNode, insertNode):
            if not curNode.left and not curNode.right:
                curNode.left = insertNode if curNode.val > insertNode.val else None
                curNode.right = insertNode if curNode.val < insertNode.val else None
                return

            if not curNode.left and curNode.val > insertNode.val:
                curNode.left = insertNode
                return
            
            if not curNode.right and curNode.val < insertNode.val:
                curNode.right = insertNode
                return
            
            if insertNode.val > curNode.val:
                helper(curNode.right, insertNode)
            else:
                helper(curNode.left, insertNode)
        helper(root, node)
        return root