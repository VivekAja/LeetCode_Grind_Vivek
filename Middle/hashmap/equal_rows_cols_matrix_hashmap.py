from collections import defaultdict
from collections import Counter
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        row_counter = Counter(tuple(row) for row in grid)
        col_counter = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))

        count = 0
        print(row_counter, col_counter)
        for col in col_counter:
            if col in row_counter:
                print(row_counter[col], col_counter[col])
                count += row_counter[col] * col_counter[col]

        return count
if __name__ == '__main__':
    grid = [[3,1,2,2],
            [1,4,4,5],
            [2,4,2,2],
            [2,4,2,2]]
    print(Solution().equalPairs(grid))
