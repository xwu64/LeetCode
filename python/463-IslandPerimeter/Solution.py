class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result += 4
                    if j-1 >=0 and grid[i][j-1] == 1:
                        result -=1
                    if i-1 >=0 and grid[i-1][j] == 1:
                        result -=1
                    if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                        result -=1
                    if i+1 < len(grid) and grid[i+1][j] == 1:
                        result -=1

        return result
