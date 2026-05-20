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
        maska = 0
        maskb = 0

        for i in range(len(A)):
            maska |= 1 << A[i]
            maskb |= 1 << B[i]

            gays_count = bin(maska & maskb).count("1")
            ans.append(gays_count)

        return ans
