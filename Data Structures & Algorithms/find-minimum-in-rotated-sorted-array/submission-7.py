class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[(l+r) // 2]
        while l <=r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] > nums[l]:
                if nums[m] < nums[r]:
                    return nums[l]
                else:
                    l = m + 1
            else:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return res