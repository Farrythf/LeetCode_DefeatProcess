class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            m = -1
            x = -x
        else:
            m = 1
        y = str(x)
        y = y[::-1]
        res = int(y) * m
        if res > 2**31-1 or res < -2**31:
            return 0
        return res