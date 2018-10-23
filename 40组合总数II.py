class Solution:
    def combinationSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def dfs(x, remain, stack):
            for c,i in enumerate(x):
                if c >= 1 and x[c] == x[c - 1]:
                    continue
                if remain - i == 0:
                    res.append(stack+[i])
                    break
                elif remain - i < 0:
                    break
                else:
                    dfs(x[c+1:], remain - i, stack + [i])
        dfs(nums, target, [])
        return res