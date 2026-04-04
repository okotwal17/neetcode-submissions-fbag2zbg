class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0]*(max(nums)+1)
        for ele in nums:
            arr[ele]+=1
        for i in range(len(arr)):
            if(arr[i] != 0 and arr[i]!=1):
                return i
        return -1;