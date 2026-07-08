"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        hashmap = {None : None}
        while cur:
            curNode = Node(cur.val)
            hashmap[cur] = curNode
            cur = cur.next
        cur = head
        while cur:
            curNode = hashmap[cur]
            curNode.random = hashmap[cur.random]
            curNode.next = hashmap[cur.next]
            cur = cur.next
        return hashmap[head]
        

            