"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        def dfs(node):
            if node in hashmap:
                return
            newNode = Node(node.val)
            hashmap[node] = newNode
            for neighbor in node.neighbors:
                dfs(neighbor)
                newNode.neighbors.append(hashmap[neighbor])
        if node:
            dfs(node)
        return hashmap[node] if node else None