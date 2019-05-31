class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        water = 0
        for a in range(len(height)):
            if height[head] > height[tail]:
                area = (tail - head) * height[tail]
                tail = tail - 1
            else:
                area = height[head] * (tail - head)
                head = head + 1
            if area > water:
                water = area
        return water