#63.不同路径 II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [[0]*m for x in range(n)]
        dp[0][0] = 1
        #print(dp)
        for i in range(0,n):
            for j in range(0,m):
                if obstacleGrid[i][j] == 1:
                    continue
                if j - 1 >=0:
                    dp[i][j] += dp[i][j-1]
                if i - 1 >=0:
                    dp[i][j] += dp[i-1][j]
        return dp[-1][-1]
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """

s = Solution()
obs = [
  [0,0,1],
  [0,1,0],
  [1,0,0]
]
t = s.uniquePathsWithObstacles(obs)
print(t)