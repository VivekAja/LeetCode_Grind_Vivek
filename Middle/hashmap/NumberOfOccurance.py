#leetcode 1207

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Step 1: Count frequencies manually
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Check if all frequency values are unique
        seen = set()
        for count in freq.items():
            print(count, freq.items())
            if count in seen:
                return False
            seen.add(count)

        return True
if __name__ == '__main__':
    arr = [1, 2, 2, 1, 1, 3]
    print(Solution().uniqueOccurrences(arr))  # Output: True
    arr = [1, 2]
    print(Solution().uniqueOccurrences(arr))  # Output: False
    arr = [-3, -3, -2, -2, -2, -1]
    print(Solution().uniqueOccurrences(arr))  # Output: False
