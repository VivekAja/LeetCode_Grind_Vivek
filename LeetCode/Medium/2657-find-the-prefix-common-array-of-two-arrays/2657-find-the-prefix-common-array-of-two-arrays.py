class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        1. Frequency mapping
        ans = []
        n = len(A)
        counts = [0] * (n+1)
        gays = 0
        for i in range(n):
            counts[A[i]] +=1 
            if counts[A[i]] == 2:
                gays +=1
            counts[B[i]] += 1
            if counts[B[i]] == 2:
                gays+=1
            ans.append(gays)
        return ans 

        TC: O(N)
        SC: O(N)

        =============================

        2. Using Set
        
        ans = []
        n = len(A)
        gays = 0
        seen = set()

        for i in range(n):
            if A[i] in seen:
                gays +=1 
            else:
                seen.add(A[i])

            if B[i] in seen:
                gays+=1
            else:
                seen.add(B[i])

            ans.append(gays)
        return ans
        TC: O(N)
        SC: O(N)

        ==================

        Bit Mask

        """
        ans = []
        seen_mask = 0
        common = 0

        for i in range(len(A)):
            # Check if A[i] was already seen in B
            if (seen_mask & (1 << A[i])) != 0:
                common += 1
            seen_mask |= 1 << A[i]  # Mark A[i] as seen

            # Check if B[i] was already seen in A
            if (seen_mask & (1 << B[i])) != 0:
                common += 1
            seen_mask |= 1 << B[i]  # Mark B[i] as seen

            ans.append(common)

        return ans
