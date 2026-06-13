class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
            
        primes = [2,3,5]
        for factor in primes:
            while n % factor == 0:
                n //= factor
                
        # If we are left with 1, it is an ugly number
        return n == 1