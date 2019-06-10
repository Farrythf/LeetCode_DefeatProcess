class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
        x = 1
        r1 = []
        r2 = []
        for i in range(n):
            for j in range(m):
                x = x and matrix[i][j]
            x = x and 1
            r1.append(x)
            x = 1
        x = 1
        for i in range(m):
            for j in range(n):
                x = x and matrix[j][i]
            x = x and 1
            r2.append(x)
            x = 1
        for i in range(n):
            for j in range(m):
                matrix[i][j] = matrix[i][j] * r1[i] * r2[j]