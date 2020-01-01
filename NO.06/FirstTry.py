class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        "numRows-1+numRows-1= 2numRows - 2"
        out = ""
        slen = len(s) - 1
        if slen < 0:
            return ""
        if numRows == 1:
            return s
        loopnum = slen/(2 * numRows - 2) + 1
        for a in range(numRows):
            for i in range(loopnum):
                if i * (2 * numRows - 2) + a > slen:
                    break
                out = out + s[i * (2 * numRows - 2) + a]
                if a != 0 and a != numRows - 1:
                    if i * (2 * numRows - 2) + (2 * numRows - 2) - a > slen:
                        break
                    out = out + s[i * (2 * numRows - 2) + (2 * numRows - 2) - a]
        return out