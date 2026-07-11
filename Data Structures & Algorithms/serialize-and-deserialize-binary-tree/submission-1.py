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
        ans = str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        print(ans)
        return ans

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        self.i = 0
        def dfs(i):
            if arr[i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(arr[i]))
            self.i += 1
            node.left = dfs(self.i)
            node.right = dfs(self.i)
            return node
        return dfs(0)