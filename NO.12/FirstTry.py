class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
        ret = ""        
        for i, j in enumerate(nums):
            while num >= j:
                ret += strs[i]
                num -= j
            if num == 0:
                return ret