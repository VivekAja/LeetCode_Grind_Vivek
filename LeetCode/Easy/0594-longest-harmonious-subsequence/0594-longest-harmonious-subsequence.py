class Solution:
    def findLHS(self, nums: List[int]) -> int:
                # Count the frequency of each number in the list using Counter
        frequency_map = Counter(nums)
      
        # Initialize the variable to store the length of the longest harmonious subsequence
        longest_harmonious_subseq_length = 0
      
        # Iterate through each number in the nums list
        for num in nums:
            # Check if the number has a companion number that is one greater
            if num + 1 in frequency_map:
                # Harmonious subsequence found with num and num + 1
                # Calculate its length: count of num + count of num + 1
                current_length = frequency_map[num] + frequency_map[num + 1]
                # Update the answer with the maximum length found so far
                longest_harmonious_subseq_length = max(longest_harmonious_subseq_length, current_length)
      
        # Return the length of the longest harmonious subsequence found
        return longest_harmonious_subseq_length