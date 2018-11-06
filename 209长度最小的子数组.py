class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        total = 0
        length = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= s:
                total -= nums[l]
                length = min(length, r - l + 1)
                l += 1
        if length == float('inf'):
            return 0
        return length