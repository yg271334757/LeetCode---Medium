class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(k, n, ans, nums):
            if k == 0 and n == 0 and ans not in res:
                res.append(ans)
                return
            elif k > 0 and n > 0:
                for i in range(len(nums)):
                    dfs(k-1, n - nums[i], ans + [nums[i]], nums[i+1:])
        dfs(k, n, [] , [1,2,3,4,5,6,7,8,9])
        return res