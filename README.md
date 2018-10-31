# LeetCode---Medium
#### [No. 3.](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  使用栈的方法
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
#### No. 46. 全排列，也可以用DFS的方法:
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
#### No. 47. 去重：
``` py
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
```
#### No. 49. Hashmap的key不能是列表
#### No. 71. Stack way
#### No. 79. 矩阵相邻元素((-1,0),(1,0),(0,-1),(0,1))
#### No. 80. 比较好的方法是:
``` py
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        idx = 0
        count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                count += 1
                if count >= 3:
                    continue
            else:
                count = 1
            nums[idx] = nums[i]
            idx += 1
        return idx
```