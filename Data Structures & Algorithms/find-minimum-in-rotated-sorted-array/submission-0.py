class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        minimum = None
        while left<=right:
            mid = (left+right)//2
            if minimum == None or nums[mid]<minimum:
                minimum = nums[mid]
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid-1
        
        return minimum