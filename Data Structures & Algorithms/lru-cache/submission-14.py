class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.leastRecent = Node(0,0)
        self.mostRecent = Node(0,0)
        self.hashmap = {}
        self.leastRecent.next = self.mostRecent
        self.mostRecent.prev = self.leastRecent
    def deleteNode(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        del self.hashmap[node.key]
    def insertNode(self, node):
        prev, next = self.mostRecent.prev, self.mostRecent
        prev.next = node
        next.prev = node
        node.next, node.prev = next, prev
        self.hashmap[node.key] = node
        
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = Node(key, self.hashmap[key].val)
        self.deleteNode(self.hashmap[key])
        self.insertNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.hashmap:
            self.deleteNode(self.hashmap[key])
            self.insertNode(node)
            return
        self.insertNode(node)
        self.size += 1
        if self.size > self.capacity:
            self.deleteNode(self.hashmap[self.leastRecent.next.key])
            self.size -= 1
