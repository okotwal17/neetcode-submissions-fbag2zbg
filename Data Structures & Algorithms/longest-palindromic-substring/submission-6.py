class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Checking string s of size n if palindrome: O(N)
        #Getting every substring: N^2
        #N^2 * N = N^3
        #N^2
        longestLen = -1
        start, end = -1, -1
        for i in range(len(s)):
            curLen = 0
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > longestLen:
                    longestLen = curLen
                    start, end = l, r
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > longestLen:
                    longestLen = curLen
                    start, end = l, r
                l -= 1
                r += 1
        return s[start: end + 1]