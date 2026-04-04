class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for curr in range(len(nums)):
            l, r = curr+1, len(nums)-1
            while l<r:
                if nums[curr]+nums[l]+nums[r]==0:
                    temp = [nums[curr],nums[l],nums[r]]
                    if temp not in res:
                        res.append(temp)
                    l+=1
                    r-=1
                elif nums[curr]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
            
        return res
                