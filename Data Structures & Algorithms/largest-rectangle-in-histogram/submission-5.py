class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = -1
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, (i - idx) * height)
                start = idx
            stack.append((start, h))
        print(maxArea, stack)
        while stack:
            idx, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - idx))
        return maxArea

            