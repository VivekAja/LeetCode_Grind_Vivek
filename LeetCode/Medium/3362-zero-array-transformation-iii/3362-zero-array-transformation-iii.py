from collections import defaultdict
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        '''
        n = len(nums)
        m = len(queries)
        nums = sorted(nums)
        if sum(nums)<=0:
            return m
        def is_possible(remove_count):
            # Try all combinations of removing 'remove_count' queries
            from itertools import combinations

            for removed in combinations(range(m), remove_count):
                removed_set = set(removed)
                freq = [0] * n
                for i, (l, r) in enumerate(queries):
                    if i in removed_set:
                        continue
                    freq[l] += 1
                    if r + 1 < n:
                        freq[r + 1] -= 1
                # prefix sum to compute how many queries affect each index
                for i in range(1, n):
                    freq[i] += freq[i - 1]
                # Check if each nums[i] <= available query count at index i
                if all(freq[i] >= nums[i] for i in range(n)):
                    return True
            return False

        # Binary search for maximum number of removable queries
        left, right, answer = 0, len(queries), -1
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer if answer != len(queries) else -1
        '''
        import heapq
        n = len(nums)
        m = len(queries)

        past = []
        maxHeap = []

        queries.sort(key = lambda x:x[0])

        j = 0
        used = 0
        for i in range(n):
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(maxHeap, -queries[j][1])  # use -end to simulate max-heap
                j += 1

            # Apply already-used queries
            nums[i] -= len(past)

            # Use more queries if needed
            while nums[i] > 0 and maxHeap and -maxHeap[0] >= i:
                r = -heapq.heappop(maxHeap)
                heapq.heappush(past, r)
                used += 1
                nums[i] -= 1

            # If we can't reduce nums[i] to 0
            if nums[i] > 0:
                return -1

            # Remove expired queries
            while past and past[0] == i:
                heapq.heappop(past)

        return len(queries) - used


    