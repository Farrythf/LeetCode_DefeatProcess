class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n = len(matrix)
        nl = n
        if n == 0:
            return []
        m = len(matrix[0])
        ml = m
        for i in matrix[0]:
            res.append(i)
        while 1:
            nl = nl -1
            if nl == 0:
                break
            for i in range(n-nl,n):
                res.append(matrix[i][m-1])
                
            ml = ml -1
            if ml == 0:
                break
            for i in range(m-2,m-ml-2,-1):
                res.append(matrix[n-1][i])
                
            nl = nl -1
            if nl == 0:
                break
            for i in range(n-2,n-nl-2,-1):
                res.append(matrix[i][m-ml-1])
                
            ml = ml -1
            if ml == 0:
                break
            for i in range(m-ml-1,m-1):
                res.append(matrix[m-ml-1][i])
                
            m = m - 1
            n = n - 1
        return res