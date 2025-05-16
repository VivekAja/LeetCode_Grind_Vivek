#BruteForce
#Time = O(N log N)
#Space = O(U)
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        return c.most_common(1)[0][0]
"""
#Boyer Moore's Voting Algo
Time = O(N)
Space = O(1)

class Solution(object):
    def majorityElement(self, nums):

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
            

"""
