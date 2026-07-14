class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        print(self.cache)
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        print(self.cache)
        if len(self.cache) > self.capacity:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)
        print(self.cache)
        
    def remove(self,node):
        node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, node):
        node.next, node.prev = self.right, self.right.prev
        self.right.prev.next, self.right.prev = node, node