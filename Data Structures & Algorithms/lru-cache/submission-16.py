class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keyToNode = {}
        self.size = 0
        self.capacity = capacity
        self.leastRecent = Node(0,0)
        self.mostRecent = Node(0,0)
        self.leastRecent.next = self.mostRecent
        self.mostRecent.prev = self.leastRecent

    def deleteNode(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        del self.keyToNode[node.key]
        self.size -= 1
    
    def insertNode(self, node):
        prev, next = self.mostRecent.prev, self.mostRecent
        node.prev = prev
        node.next = next
        next.prev = node
        prev.next = node
        self.keyToNode[node.key] = node
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        node = Node(key, self.keyToNode[key].val)
        self.deleteNode(self.keyToNode[key])
        self.insertNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.keyToNode:
            self.deleteNode(self.keyToNode[key])
        self.insertNode(node)
        if self.size > self.capacity:
            self.deleteNode(self.leastRecent.next)
