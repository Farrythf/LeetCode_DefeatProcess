class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        sepe = []
        while x >= 10:
            sepe.append(x % 10)
            x = x / 10
        sepe.append(x)
        for i in range(len(sepe)):
            if sepe[i] != sepe[len(sepe) - i - 1]:
                return False
        return True