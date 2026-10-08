class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        hashset = set()
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            maxLen = max(maxLen, r - l + 1)
            hashset.add(s[r])
        return maxLen
        
