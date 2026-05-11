class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        MAX_VAL = max(nums) + 1

        # Step 1: Sieve of Eratosthenes for smallest prime factor (SPF)
        spf = list(range(MAX_VAL))
        for i in range(2, int(MAX_VAL**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, MAX_VAL, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x >= 2 and spf[x] == x

        def prime_factors(x):
            """Return set of distinct prime factors of x."""
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors

        # Step 2: Build prime -> list of indices map
        # For each index j, for each prime p dividing nums[j], record j
        prime_to_indices = defaultdict(list)
        for j, val in enumerate(nums):
            for p in prime_factors(val):
                prime_to_indices[p].append(j)

        # Step 3: BFS
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()

                if i == n - 1:
                    return steps

                # Adjacent steps
                for nb in (i - 1, i + 1):
                    if 0 <= nb < n and not visited[nb]:
                        visited[nb] = True
                        queue.append(nb)

                # Prime teleportation: only if nums[i] itself is prime
                if is_prime(nums[i]):
                    p = nums[i]
                    if p in prime_to_indices:
                        for j in prime_to_indices[p]:
                            if not visited[j]:
                                visited[j] = True
                                queue.append(j)
                        # Crucial: delete so we never re-expand this group
                        del prime_to_indices[p]

            steps += 1

        return steps  # unreachable given valid input