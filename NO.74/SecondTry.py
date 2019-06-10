class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        min = 0 
        max = len(matrix) - 1
        
        while(min >= max):
            if(target in matrix[min]):
                return True
            else: min+=1
             
            if(target in matrix[max]):
                return True
            else: max-=1
        
        return False