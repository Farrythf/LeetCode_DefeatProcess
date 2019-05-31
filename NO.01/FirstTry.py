class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1,a in enumerate(nums):
            for index2,i in enumerate(nums):
                if((a + i == target) and (index1!=index2)):
                    return [index1, index2];
        