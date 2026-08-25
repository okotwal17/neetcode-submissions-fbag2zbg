class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        #Reversal
        l, r = 0, len(nums) - 1
        for i in range(len(nums) // 2):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        #Left reversal
        l, r = 0, k - 1
        for i in range(k // 2):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        #Right reversal
        l, r = k, len(nums) - 1
        for i in range((len(nums) - k) // 2):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        


            