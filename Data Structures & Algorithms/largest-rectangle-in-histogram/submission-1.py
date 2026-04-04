class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            idx=i
            while len(stack)>0 and stack[-1][1]>heights[i]:
                tup = stack.pop()
                maxArea = max(maxArea, tup[1]*(i-tup[0]))
                idx=tup[0]
            pair = (idx,heights[i])
            stack.append(pair)
        while len(stack)!=0:
            tup = stack.pop()
            maxArea = max(maxArea, tup[1]*(len(heights)-tup[0]))
        return maxArea