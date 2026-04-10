class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        h = int(n/2)
        s1 = nums[:h]
        s2 = nums[h:]
        res = []
        for i in range(len(s1)):
            res.append(s1[i])
            res.append(s2[i])
        
        return res

