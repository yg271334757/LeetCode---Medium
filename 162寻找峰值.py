class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        for i in range(0, l):
            if i == 0 and nums[i] > nums[i+1]:
                return 0
            elif i == l-1 and nums[i] > nums[i-1]:
                return l-1
            elif nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i