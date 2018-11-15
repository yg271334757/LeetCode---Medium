from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b = sorted(Counter(nums).items(), key=lambda x: x[1])
        return [b[0][0], b[1][0]]