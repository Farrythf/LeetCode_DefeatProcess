class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        i = len(obstacleGrid[0])
        j = len(obstacleGrid)
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for n in range(1,i):
            if obstacleGrid[0][n] == 0:
                obstacleGrid[0][n] = obstacleGrid[0][n-1]
            elif obstacleGrid[0][n] == 1:
                obstacleGrid[0][n] = 0;
        for n in range(1,j):
            if obstacleGrid[n][0] == 0:
                obstacleGrid[n][0] = obstacleGrid[n-1][0]
            elif obstacleGrid[n][0] == 1:
                obstacleGrid[n][0] = 0;
        for n in range(1,i):
            for m in range(1,j):
                if obstacleGrid[m][n] == 1:
                    obstacleGrid[m][n] = 0;
                else:
                    obstacleGrid[m][n] = obstacleGrid[m-1][n] + obstacleGrid[m][n-1]
        return obstacleGrid[j-1][i-1]