class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        l = len(nums)
        res = []
        for i in range(l+1):
            for j in combinations(nums,i):
                res.append(list(j))
        return res