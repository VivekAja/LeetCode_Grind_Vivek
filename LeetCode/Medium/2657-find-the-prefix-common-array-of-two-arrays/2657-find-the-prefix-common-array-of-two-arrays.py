class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
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