# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #1L2LNRNR3L4LNRNR5LNRN
        dataList = data.split(",")
        self.idx = 0
        def dfs():
            if dataList[self.idx] == "N":
                return None
            node = TreeNode(int(dataList[self.idx]))
            self.idx += 1
            node.left = dfs()
            self.idx += 1
            node.right = dfs()
            return node
        return dfs()

        
        
