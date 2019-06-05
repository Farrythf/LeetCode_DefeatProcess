class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        length = m + n - 2
        mol = length
        deno = m - 1
        for i in range(m-2):
            mol = mol * (length - 1)
            length = length - 1
        for i in range(m-2):
            deno = deno * (m-2)
            m = m - 1
        res = int(mol / deno)
        return res