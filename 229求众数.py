from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) // 3
        times = Counter(nums)
        return [k[0] for k in times.items() if k[1] > n]