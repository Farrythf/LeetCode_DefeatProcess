class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        "numRows-1+numRows-1= 2numRows - 2"
        if numRows ==1:
            return s
        temp = numRows * [""]
        out = ""
        forward = True
        backward = False
        num = 0
        for i in s:
            temp[num] += i
            if forward:
                num += 1
            elif backward:
                num -= 1
            if num == numRows - 1:
                forward = False
                backward = True
            elif num == 0:
                forward = True
                backward = False
        for i in temp:
            out = out + i
        return out