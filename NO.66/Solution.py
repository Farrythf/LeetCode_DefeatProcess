class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for digit in digits:
            num = num*10 + digit
        
        num += 1
        
        ret = []
        while num > 0:
            ret = [num%10] + ret
            num = num / 10
        
        return ret