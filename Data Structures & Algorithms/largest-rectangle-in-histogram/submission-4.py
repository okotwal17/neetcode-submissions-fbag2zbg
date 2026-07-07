class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                idx, val = stack.pop()
                res = max(res, (i - idx) * val)
                start = idx
            stack.append((start, v))
        
        while stack:
            idx, val = stack.pop()
            res = max(res, (len(heights) - idx) * val)
        return res
