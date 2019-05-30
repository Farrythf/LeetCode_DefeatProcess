class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = -999
        tmp = 0
        h = 0
        t = length - 1
        while t >= h:
            if nums[t] < 0:
                t = t - 1
                continue
            if nums[h] < 0:
                h = h + 1
                continue
            for i in range(h,t+1):
                tmp = tmp + nums[i]
            if tmp > res:
                res = tmp
            tmp = 0
            if t == h:
                h = h + 1
                t = length - 1
            else:
                t = t - 1
        if res == -999:
            res = nums[0]
            for tmp in nums:
                if tmp > res:
                    res = tmp
        return res