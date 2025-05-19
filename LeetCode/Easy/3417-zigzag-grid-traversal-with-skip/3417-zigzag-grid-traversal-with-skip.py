class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        ans = []
        tricks = True
        for i in range(m):
            if i%2 ==0:
                for j in range(n):
                    if tricks:
                        ans.append(grid[i][j])
                    tricks = not tricks
            else:
                        
                for j in range(n-1,-1,-1):
                    if tricks:
                        ans.append(grid[i][j])
                    tricks = not tricks
        return ans
                