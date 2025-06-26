class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        subsequence_length = value_so_far = 0
      
        # Iterate over the string in reverse order since the least significant bit contributes less to the overall value
        for character in reversed(s):
            # If the character is '0', it doesn't affect the value but can increase the length of the subsequence
            if character == "0":
                subsequence_length += 1
            # If the character is '1', check if adding this bit exceeds the value of k
            # Since we're looking at the binary string from right to left, we shift 1 left by the current subsequence length
            # The subsequence_length represents the binary digit's position (0-indexed)
            # Also note that we perform this check only if subsequence_length is less than 30 since 2^30 is the first power of 2 that exceeds 10^9 (~2^30.103). k is less than or equal to 10^9
            elif subsequence_length < 30 and (value_so_far | (1 << subsequence_length)) <= k:
                # If adding '1' to the current position does not exceed k, update the value_so_far
                value_so_far |= 1 << subsequence_length
                # Increase subsequence_length as this '1' is part of the longest subsequence not exceeding k
                subsequence_length += 1
              
        # Return the length of the longest subsequence not exceeding the value k
        return subsequence_length