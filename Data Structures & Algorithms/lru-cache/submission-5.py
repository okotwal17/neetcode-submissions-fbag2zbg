class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            temp = self.hashmap.pop(key)
            self.hashmap[key] = temp
            return temp
        return -1       

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)
            self.hashmap[key] = value
        else:
            self.hashmap[key] = value
            self.size+=1
            if self.capacity==self.size:
                for k,v in self.hashmap.items():
                    self.hashmap.pop(k)
                    break
