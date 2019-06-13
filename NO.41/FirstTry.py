class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        nums.sort()
        if nums[-1] <= 0:
            return 1
        i = 0
        res = 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            if res == nums[i]:
                res+=1
            elif res > nums[i]:
                continue
            else:
                return res
        return res