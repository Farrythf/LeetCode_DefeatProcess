class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new = []
        for i in range(0,n):
            for a in range(n-1,-1,-1):
                new.append(matrix[a][i])
            matrix.append(new)
            new = []
        del matrix[0:n]