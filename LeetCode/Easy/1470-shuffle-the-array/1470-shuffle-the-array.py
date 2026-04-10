class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s1 = nums[:int(len(nums)/2)]
        s2 = nums[int(len(nums)/2):]
        res = []
        for i in range(len(s1)):
            res.append(s1[i])
            res.append(s2[i])
        
        return res

