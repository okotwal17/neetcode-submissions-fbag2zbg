class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                #l-->m-->target
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                #target<--m<--r
                if target > nums[r] or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return -1