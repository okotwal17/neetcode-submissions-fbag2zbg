class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        temp = self.dictionary.get(key, [])
        temp.append((value, timestamp))
        self.dictionary[key] = temp

    def get(self, key: str, timestamp: int) -> str:
        res, curKeys = "", self.dictionary.get(key, [])
        l, r = 0, len(curKeys) - 1
        while l <= r:
            mid = (l+r) // 2
            if curKeys[mid][1] <= timestamp:
                res = str(curKeys[mid][0])
                l = mid +1
            else:
                r = mid - 1
        return res
