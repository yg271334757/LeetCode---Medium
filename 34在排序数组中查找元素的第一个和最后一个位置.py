class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        res = []
        n = nums.count(target)
        l = len(nums)
        while i < l:
            if nums[i] == target:
                res.append(i)
                res.append(i + n - 1)
                return res
            i += 1
        return[-1,-1]