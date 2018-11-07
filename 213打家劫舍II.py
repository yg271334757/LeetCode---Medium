class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        def rubber(x):
            res = [0] * len(x)
            res[0] = x[0]
            res[1] = max(x[0], x[1])
            for i in range(2, len(x)):
                res[i] = max(res[i - 1], res[i - 2] + x[i])
            return res[-1]
        return max(rubber(nums[1:]), rubber(nums[:-1]))