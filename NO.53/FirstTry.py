class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = 0
        tmp = 0
        h = 0
        t = length - 1
        while t >= h:
            if nums[h] < 0:
                h = h + 1
                continue
            if nums[t] < 0:
                t = t - 1
                continue
            for i in range(h,t):
                tmp = tmp + nums[i]
            if tmp > res:
                res = tmp
                tmp = 0
        return res