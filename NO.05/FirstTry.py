class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len = self.h(i,s,1)
            if cur_len > max_len:
                out = s[i-(cur_len-1)/2:i+(cur_len-1)/2+1]
                max_len = cur_len
        for i in range(len(s)):
            cur_len = self.hh(i,s,1)
            if cur_len > max_len:
                out = s[i - cur_len/2 + 1:i+cur_len/2+1]
                max_len = cur_len
        return out
    
    def h(self,i,s,k):
        if i-k < 0 or i+k >= len(s):
            return 2*(k-1)+1
        elif s[i-k] != s[i+k]:
            return 2*(k-1)+1
        else:
            return self.h(i,s,k+1)
    
    def hh(self,i,s,k):
        if i-k+1 < 0 or i+k >= len(s):
            return 2*(k-1)
        elif s[i-k+1] != s[i+k]:
            return 2*(k-1)    
        else:
            return self.hh(i,s,k+1)