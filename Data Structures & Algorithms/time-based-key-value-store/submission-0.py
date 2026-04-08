class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curKey = self.hashmap.get(key,[])
        curKey.append((timestamp, value))
        self.hashmap[key] = curKey

    def get(self, key: str, timestamp: int) -> str:
        if len(self.hashmap.get(key, [])) == 0:
            return ""
        keyList = self.hashmap[key]
        l, r = 0, len(keyList)
        while l < r:
            mid = (l + r) // 2
            if keyList[mid][0] == timestamp:
                return keyList[mid][1]
            elif keyList[l][0] < keyList[mid][0]:
                r = mid - 1
            else:
                l = mid +1
        print('Out of loop')
        return keyList[l-1][1]

