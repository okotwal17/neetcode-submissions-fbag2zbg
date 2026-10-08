class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        maxLen = 3
        set = (z, x, y)
        windowSize = r - l + 1
        zxyzxyz
        l  r
        """
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
        
