class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        M = 10**9 + 7

        if k > len(word):
            return 0

        # Step 1: Count frequency blocks of consecutive identical characters
        freq = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)

        # Step 2: Calculate total possible combinations (P)
        P = 1
        for f in freq:
            P = (P * f) % M

        if len(freq) >= k:
            return P

        n = len(freq)

        # Step 3: DP table t[i][count] = number of invalid ways from index i with current count
        t = [[0] * (k + 1) for _ in range(n + 1)]

        for count in range(k - 1, -1, -1):
            t[n][count] = 1

        for i in range(n - 1, -1, -1):
            prefix = [0] * (k + 2)
            for h in range(1, k + 1):
                prefix[h] = (prefix[h - 1] + t[i + 1][h - 1]) % M

            for count in range(k - 1, -1, -1):
                l = count + 1
                r = count + freq[i]
                r = min(r, k - 1)

                if l <= r:
                    t[i][count] = (prefix[r + 1] - prefix[l] + M) % M

        invalid_count = t[0][0]
        return (P - invalid_count + M) % M