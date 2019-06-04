class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        tem = []
        if n == 1:
            return [[1]]
        if n == 0:
            return [[]]
        for a in range(1,n+1):
            tem.append(a)
        for i in range(n):
            res.append(list(tem))
        nl = n
        while 1:
            nl = nl -1
            if nl == 0:
                break
            for i in range(n-nl,n):
                a = a + 1
                res[i][n-1] = a
            for i in range(n-2,n-nl-2,-1):
                a = a + 1
                res[n-1][i] = a
            nl = nl -1
            if nl == 0:
                break
            for i in range(n-2,n-nl-2,-1):
                a = a + 1
                res[i][n-nl-2] = a
            for i in range(n-nl-1,n-1):
                a = a + 1
                res[n-nl-1][i] = a
            n = n - 1
        return res