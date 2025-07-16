class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        eves = 0
        odds = 0
        alts = 1
        for n in nums:
            if n %2 == 0:
                eves+=1
            else:
                odds +=1
        #return max(eves, odds)
        p = nums[0]%2
        '''
        for i in range(1, len(nums)-1):
            if (nums[i] + nums[i-1]) % 2 == 1:
                alts +=1
            else:
                nums.pop(i)
        return max( eves, odds, alts+1)
        '''
        for i in range(1, len(nums)):
            curr = nums[i]%2
            if curr != p:
                alts+=1
                p = curr
        return max( eves, odds, alts)