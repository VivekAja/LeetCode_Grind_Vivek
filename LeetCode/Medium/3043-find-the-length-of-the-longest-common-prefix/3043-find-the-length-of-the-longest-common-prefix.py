class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        1. Brute Force - Works but very inefficient
        count, maxi = 0, 0

        for a in arr1:
            a= str(a)
            for b in arr2:
                b = str(b)
                i, j = 0, 0
                while i<len(a) and j <len(b):
                    if a[i] == b[i]:
                        count+=1
                    else:
                        break
                    #print(i,j, a[i], b[j], count)
                    i+=1
                    j+=1
                maxi = max(count, maxi)
                count= 0
            #print(f'max and count:{maxi}, {count}')

        return maxi
        TC: O(N*M)
        SC: O(N*M)

        2. Hashmap
        """

        maxi = 0
        pre = set()
        for a in arr1:
            while a:
                pre.add(a)
                a //= 10
        
        for b in arr2:
            while b:
                if b in pre:
                    maxi = max(maxi, len(str(b)))
                    break
                b //= 10
                
        return maxi

