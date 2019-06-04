class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1:
            return 1
        elif m == 2:
            return n
        elif m == 3:
            return int(0.5*n*(n+1))
        elif n == 1:
            return 1
        elif n == 2:
            return m
        elif n == 3:
            return int(0.5*m*(m+1))
        else:
            res = 0
            for i in range(1,m+1):
                res = res + self.uniquePaths(i, n-1)
            return res
        