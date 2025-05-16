class Solution(object):
    def fractralGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[0]]

        prev = self.fractralGrid(n - 1)
        size = len(prev)


        # Create an empty 2^n x 2^n grid
        grid = [[0] * (2 * size) for _ in range(2 * size)]

        for i in range(size):
            for j in range(size):
                val= prev[i][j]
                grid[i][j] = val
                grid[i][j + size] = prev[i][size - 1 - j]
                grid[i + size][j] = prev[size - i - 1][j]
                grid[i + size][j + size] = val^1

        return grid
if __name__ == '__main__':
    n = 3
    print(Solution().fractralGrid(n))