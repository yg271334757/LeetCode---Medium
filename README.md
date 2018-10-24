# LeetCode---Medium
#### No. 3.  使用栈的方法
#### No. 31. 原来函数还可以这样用
#### No. 36. 创建二维数组： a = [[[0] for _ in range(3)] for _ in range(3)]
#### No. 39. DFS
``` python
    def dfs(remain, stack):
        if not remain:
            res.append(stack)
            return 
        for item in candidates:
            if item > remain:
                break
            elif not stack or item >= stack[-1]:
                dfs(remain - item, stack + [item])
```
#### No. 40. DFS
``` python
        def dfs(x, remain, stack):
            for c,i in enumerate(x):
                if c >= 1 and x[c] == x[c - 1]: #去除重复的元素
                    continue
                if remain - i == 0:
                    res.append(stack+[i])
                    break
                elif remain - i < 0:
                    break
                else:
                    dfs(x[c+1:], remain - i, stack + [i])
```
#### No. 40. 全排列，也可以用DFS的方法:
``` python
class Solution:
    def permute(self, nums):
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
                dfs(x[:i] + x[i+1:], stack+[v])
        dfs(nums, [])
        return res
```