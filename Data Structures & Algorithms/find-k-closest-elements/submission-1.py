class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = deque()
        for i in range(k):
            q.append(arr[i])
        for i in range(k, len(arr)):
            a, b = q[0], arr[i]
            if abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b):
                return list(q)
            else:
                q.popleft()
                q.append(b)
        return list(q)