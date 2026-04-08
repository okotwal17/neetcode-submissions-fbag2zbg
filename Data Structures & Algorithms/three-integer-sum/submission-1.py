class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if a>0:
                break;
            if i>0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    temp = [nums[i],nums[l],nums[r]]
                    res.append(temp)
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
            
        return res
                