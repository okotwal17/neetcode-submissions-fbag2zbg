class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquared(n)
            print(n)
            if n == 1:
                return True
            
        return False
        
    def sumOfSquared(sel,n):
        res = 0
        while n != 0:
            digit = n % 10
            digit = digit**2
            res+=digit
            n = n // 10
        return res
