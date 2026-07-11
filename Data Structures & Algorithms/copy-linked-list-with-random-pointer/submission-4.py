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
        hashmap = {None : None}
        cur = head
        while cur:
            node = Node(cur.val)
            hashmap[cur] = node
            cur = cur.next

        cur = head
        while cur:
            node = hashmap[cur]
            node.next = hashmap[cur.next]
            node.random = hashmap[cur.random]
            cur = cur.next
        return hashmap[head]