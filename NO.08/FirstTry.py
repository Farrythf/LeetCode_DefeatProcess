class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = -1
        end = len(str)
        out = 0
        if end ==0:
            return 0
        for i in range(len(str)):
            if start<0 and str[i] != ' ':
                if (ord(str[i]) - ord('0') <= 9 and ord(str[i]) - ord('0') >= 0) or str[i] == '-' or str[i] == '+':
                    start = i
                else:
                    return 0
            elif start >= 0 and (ord(str[i]) - ord('0') > 9 or ord(str[i]) - ord('0') < 0):
                end = i
                break
        if start == -1:
            return 0
        target = str[start:end]
        if target[0] == '-':
            minus = 1
        elif target[0] == '+':
            minus = 2
        else:
            minus = 0
        if minus == 1:
            for i in range(len(target) - 1):
                out = out + pow(10,i) * (ord(target[len(target)-i-1]) - ord('0'))
            out = out * -1
        elif minus == 2:
            for i in range(len(target) - 1):
                out = out + pow(10,i) * (ord(target[len(target)-i-1]) - ord('0'))
        else:
            for i in range(len(target)):
                out = out + pow(10,i) * (ord(target[len(target)-i-1]) - ord('0'))
        if out >= 2147483648:
            out = 2147483648 - 1
        elif out < -2147483648:
            out = -2147483648
        return out