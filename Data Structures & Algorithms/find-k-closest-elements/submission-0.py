from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        tmp = 0
        #Populating deque
        while tmp != k:
            res.append(arr[tmp])
            tmp += 1
        for i in range(k, len(arr)):
            distCur, distRes = abs(arr[i] - x), abs(res[0] - x)
            if distRes < distCur or (distRes == distCur and res[0] < arr[i]):
                break
            res.popleft()
            res.append(arr[i])
        return list(res)
        