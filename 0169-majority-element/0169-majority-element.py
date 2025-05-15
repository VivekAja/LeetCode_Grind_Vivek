class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_highest = None
        count = 0
        
        for number in nums:
            if count == 0:
                current_highest = number
                count = 1
            elif number == current_highest:
                count += 1
            else:
                count-=1
        return current_highest
            