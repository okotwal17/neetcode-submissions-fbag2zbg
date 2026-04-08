class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,1
        maxWater = 0
        while(r<len(heights)):
            if(heights[l] < heights[r]):
                l=r
            elif(maxWater<=(r-l)*heights[r]):
                maxWater = (r-l)*heights[r]
            r+=1
        print(f"r-l is {r-l-1} and heights[r] is {heights[r-1]}")
        return maxWater