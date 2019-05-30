def canJump(self, nums):
    return reduce(lambda m, (i, n): max(m, i+n) * (i <= m), enumerate(nums, 1), 1) > 0