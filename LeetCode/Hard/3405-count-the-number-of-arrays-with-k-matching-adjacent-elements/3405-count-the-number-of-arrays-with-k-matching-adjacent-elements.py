class Solution:
    # Define MOD as a class attribute or a global constant.
    # Class attribute means it's accessed via self.MOD
    MOD = 10**9 + 7 

    # Binary exponentiation: a^b % MOD
    # No significant change needed here, it's already efficient.
    def power(self, a: int, b: int) -> int:
        result = 1
        a %= self.MOD # Ensure 'a' is within modulo range at the start
        while b > 0:
            if (b & 1) == 1: # If b is odd
                result = (result * a) % self.MOD
            a = (a * a) % self.MOD # Square 'a'
            b >>= 1 # Right shift b (divide by 2)
        return result

    # nCr % MOD using precomputed factorials and Fermat's inverse
    # This function is fine; it's O(1) after precomputation.
    def nCr(self, n: int, r: int, fact: list[int], invFact: list[int]) -> int:
        if r < 0 or r > n:
            return 0
        
        # Calculate (fact[n] * invFact[n-r] % MOD * invFact[r] % MOD)
        # Using intermediate modulo operations to prevent overflow before final modulo
        term1 = (fact[n] * invFact[n - r]) % self.MOD
        result = (term1 * invFact[r]) % self.MOD
        return result

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # Edge case: If n-1 < k, it's impossible to choose k positions.
        # This is implicitly handled by nCr returning 0, but good to be explicit.
        if k < 0 or k > n - 1:
            return 0 # Or handle based on specific problem constraints if different

        # Precompute factorials
        # Initialize with size n+1 directly to avoid dynamic resizing costs if possible
        fact = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % self.MOD

        # Precompute inverse factorials using Fermat's Little Theorem
        # invFact[i] = power(fact[i], MOD - 2)
        invFact = [0] * (n + 1)
        # Optimized: invFact[n] can be computed first using power, then others backwards
        # This uses invFact[i-1] = invFact[i] * i % MOD
        invFact[n] = self.power(fact[n], self.MOD - 2)
        for i in range(n - 1, -1, -1): # Iterate downwards from n-1 to 0
             invFact[i] = (invFact[i + 1] * (i + 1)) % self.MOD


        # Calculate result
        # Step 1: Combinations (n-1 choose k)
        result = self.nCr(n - 1, k, fact, invFact)
        
        # Step 2: Multiply by 'm' for the first element's choice
        result = (result * m) % self.MOD
        
        # Step 3: Multiply by (m - 1)^(n - k - 1) for the remaining elements
        # (n - k - 1) elements must be different from the first element's value.
        remaining_elements_count = n - k - 1

        if remaining_elements_count > 0:
            base_for_power = m - 1
            # If m-1 is 0, and remaining_elements_count > 0, then 0 to any positive power is 0.
            # This is handled correctly by self.power(0, positive_exponent) which returns 0.
            result = (result * self.power(base_for_power, remaining_elements_count)) % self.MOD
        elif remaining_elements_count == 0:
            # If exponent is 0, the term is 1 (except 0^0 which is typically 1 in combinatorics context).
            # self.power(X, 0) correctly returns 1.
            pass # No change needed as power(base, 0) returns 1, effectively multiplying by 1.
        # No else for remaining_elements_count < 0 as 'k' should be less than 'n'.
        # If k == n, then remaining_elements_count is -1, which means (n-k-1) should be 0 or more.
        # This implies k must be <= n-1. We already have 'if k > n-1: return 0'.

        return int(result)