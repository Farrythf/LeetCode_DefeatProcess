class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        max1 = len(matrix) - 1
        min1 = 0
        if max1 == -1:
            return 0
        l = len(matrix[0]) - 1
        if l == -1:
            return 0
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return 0
        while max1 > min1:
            cent1 = int((max1+min1)/2)
            if target > matrix[cent1][-1]:
                min1 = cent1 + 1
            elif target < matrix[cent1][0]:
                max1 = cent1 - 1
            else:
                break
        d1 = int((max1+min1)/2)
        if target in matrix[d1]:
            return 1
        else:
            return 0