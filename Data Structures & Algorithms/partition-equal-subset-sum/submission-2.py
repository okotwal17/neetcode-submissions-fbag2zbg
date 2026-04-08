class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNum = sum(nums)
        if sumNum % 2 == 1:
            return False
        target = sumNum / 2
        s = set()
        s.add(0)
        for num in nums:
            newSet = set()
            for ele in s:
                if num + ele == target:
                    return True
                newSet.add(num+ele)
                newSet.add(ele)
            s = newSet
        return False