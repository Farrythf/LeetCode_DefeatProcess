class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        res = [0 for _ in range(0, n)]
        res[0] = 1
        for i in range(0, m):
            for j in range(1, n):
                res[j] += res[j-1]
        return res[n-1]