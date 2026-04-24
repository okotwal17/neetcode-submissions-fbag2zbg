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
        cloneMapping = {}
        def dfs(n):
            if n is None:
                return None
            if n in visited:
                return cloneMapping[n]
            newNode = Node(n.val,[])
            visited.add(n)
            cloneMapping[n] = newNode
            for neighbor in n.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        return dfs(node)
