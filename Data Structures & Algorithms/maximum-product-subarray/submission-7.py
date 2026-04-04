class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct, minProduct = 1,1
        res = float("-inf")
        for num in nums:
            if num == 0:
                print(res)
                res = max(res, num)
                maxProduct, minProduct = 1,1
                continue
            tmp = num*maxProduct
            maxProduct = max(num*maxProduct, num*minProduct, num)
            minProduct = min(tmp, num*minProduct, num)
            res = max(res, maxProduct)
        return res