class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curSize = 0
        self.hashmap = {}

    def get(self, key: int) -> int:
        print(self.hashmap.get(key,-1))
        return self.hashmap.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)
            self.hashmap[key] = value
            print(key in self.hashmap)
        else:
            self.hashmap[key] = value
            self.curSize += 1
        if self.curSize > self.capacity:
            for k,v in self.hashmap.items():
                self.hashmap.pop(k)
                self.curSize-=1
                break
        

