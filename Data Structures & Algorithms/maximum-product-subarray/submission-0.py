class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct, minProduct = 1,1
        res = maxProduct
        for num in nums:
            if num == 0:
                maxProduct, minProduct = 1,1
            maxProduct = max(num*maxProduct, num*minProduct, num)
            minProduct = min(num*maxProduct, num*minProduct, num)
        return maxProduct