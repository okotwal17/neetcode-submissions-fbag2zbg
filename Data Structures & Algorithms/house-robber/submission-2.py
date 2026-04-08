class Solution:
    def rob(self, nums: List[int]) -> int:
        odd, even = 1, 0
        oddMoney, evenMoney = 0,0
        while odd < len(nums):
            oddMoney += nums[odd]
            odd += 2
        while even < len(nums):
            evenMoney += nums[even]
            even += 2
        print(oddMoney, evenMoney)
        return max(oddMoney, evenMoney)