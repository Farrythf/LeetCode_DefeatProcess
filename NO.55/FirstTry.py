class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = 1              
        for i in range(len(nums) - 1):
            if nums[i] != 0:
                continue
            res = 0
            for a in range(i-1,-1,-1):
                if nums[a] > i-a:
                    res = 1
                    break
            if res == 0:
                return res
        return res