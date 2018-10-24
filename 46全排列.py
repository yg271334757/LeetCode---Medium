from itertools import permutations
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = list(permutations(nums))
        return a