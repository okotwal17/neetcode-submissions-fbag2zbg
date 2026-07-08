class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        l, r = 0, len(arr) - 1
        res = ("", -1)
        while l <= r:
            m = (l + r) // 2
            val, time = arr[m]
            if time <= timestamp:
                if res[1] < time:
                    res = (val, time)
                l = m + 1
            else:
                r = m - 1

        return res[0]
        
