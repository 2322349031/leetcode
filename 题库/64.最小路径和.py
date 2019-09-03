#64. 最小路径和

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row==0 and col == 0:
                    continue
                #temp = 2**32
                if row == 0:
                    temp = grid[row][col-1]
                elif col == 0:
                    temp = grid[row-1][col]
                else:
                    temp = min(grid[row][col-1],grid[row-1][col])
                grid[row][col] += temp
        return grid[-1][-1]