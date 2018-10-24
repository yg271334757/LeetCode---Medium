class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def dfs(x,stack):
            if len(x) == 0:
                res.append(stack)
                return
            for i, v in enumerate(x):
                if i < len(x) - 1 and x[i] == x[i+1]: # 去重
                    continue
                dfs(x[:i] + x[i+1:], stack+[v])
        dfs(nums, [])
        return res