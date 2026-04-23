"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        cloneMap = {}
        def dfs(node):
            if node is None:
                return None
            if node in cloneMap or node.val in visited:
                return cloneMap[node]
            newNode = Node(node.val, [])
            cloneMap[node] = newNode
            for n in node.neighbors:
                temp = dfs((n))
                if temp is not None:  
                    newNode.neighbors.append(temp)
            visited.add(node.val)
            return newNode
        res = dfs(node)   
        return res        
            
