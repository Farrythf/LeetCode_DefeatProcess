class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch2idx = {};
        maxLen = resStart = 0;
        for i, ch in enumerate(s):
            if ch in ch2idx:
                maxLen = max(maxLen, i - resStart);
                resStart = max(resStart, ch2idx[ch] + 1);
            ch2idx[s[i]] = i;
        return max(maxLen, len(s) - resStart);