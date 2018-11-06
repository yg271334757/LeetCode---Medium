# LeetCode---Medium
#### [No. 3.](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)  使用栈的方法
#### [No. 31.](https://leetcode-cn.com/problems/next-permutation/) 原来函数还可以这样用
#### [No. 36.](https://leetcode-cn.com/problems/valid-sudoku/description/) 创建二维数组： a = [[[0] for _ in range(3)] for _ in range(3)]
#### [No. 39.](https://leetcode-cn.com/problems/combination-sum/) DFS
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
#### [No. 40.](https://leetcode-cn.com/problems/combination-sum-ii/) DFS
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
#### [No. 46.](https://leetcode-cn.com/problems/permutations/description/) 全排列，也可以用DFS的方法:
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
#### [No. 47.](https://leetcode-cn.com/problems/permutations-ii/) 去重：
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
#### [No. 49.](https://leetcode-cn.com/problems/group-anagrams/) Hashmap的key不能是列表
#### [No. 71.](https://leetcode-cn.com/problems/simplify-path/) Stack way
#### [No. 79.](https://leetcode-cn.com/problems/word-search/) 矩阵相邻元素((-1,0),(1,0),(0,-1),(0,1))
#### [No. 80.](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/) 比较好的方法是:
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
#### [No. 130.](https://leetcode-cn.com/problems/surrounded-regions/description/) DFS:
```py
r = len(board)
        c = len(board[0])
        def dfs(board, y, x):
            if x < 0 or x >= c or y < 0 or y >= r or board[y][x] != 'O':
                return 
            board[y][x] = 'S'
            dfs(board, y + 1, x)
            dfs(board, y - 1, x)
            dfs(board, y, x + 1)
            dfs(board, y, x - 1)
        for i in range(c):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[r-1][i] == 'O':
                dfs(board, r-1, i)
        for j in range(r):
            if board[j][0] == 'O':
                dfs(board, j, 0)
            if board[j][c-1] == 'O':
                dfs(board, j, c-1)
        for y in range(r):
            for x in range(c):
                if board[y][x] == 'S':
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'
```
#### [No. 131.](https://leetcode-cn.com/problems/palindrome-partitioning/description/) DFS
``` py
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def isp(x):
            return x == x[::-1]
        def dfs(x, stack):
            if not x:
                res.append(stack)
                return
            for i in range(1, len(x) + 1):
                if isp(x[:i]):
                    dfs(x[i:], stack + [x[:i]])
        dfs(s, [])
        return res
```
#### [No. 179.](https://leetcode-cn.com/problems/largest-number/description/) 排序key的使用方法,配合lambda使用：
```py
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int(''.join(sorted(map(str, nums), key=lambda s:s*6)[::-1])))
```
#### [No. 200.](https://leetcode-cn.com/problems/number-of-islands/description/) DFS和BFS， 两种不同的方法:
##### DFS:
```py
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        def fd(grid,x,y,r,c):
            grid[x][y]='-1'
            if x>0 and grid[x-1][y]=='1':
                fd(grid,x-1,y,r,c)
            if x<r-1 and grid[x+1][y]=='1':
                fd(grid,x+1,y,r,c)
            if y>0 and grid[x][y-1]=='1':
                fd(grid,x,y-1,r,c)
            if y<c-1 and grid[x][y+1]=='1':
                fd(grid,x,y+1,r,c)
        r,c=len(grid),len(grid[0])
        count = 0
        for x in range(r):
            for y in range(c):
                if grid[x][y]=='1':
                    fd(grid,x,y,r,c)
                    count += 1
        return count
```
##### BFS:
```py
from collections import deque
class Solution:
    def numIslands(self, grid):
        count = 0
        if not grid:
            return count
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    continue
                count += 1
                dq = deque([(i, j)])
                while dq:
                    p, q = dq.popleft() # 将访问过的元素置'0'
                    if p - 1 >= 0 and grid[p-1][q] == '1' and (p-1, q) not in dq:
                        dq.append((p-1, q))
                        grid[p-1][q] = '0'
                    if p + 1 < r and grid[p+1][q] == '1' and (p+1, q) not in dq:
                        dq.append((p+1, q))
                        grid[p+1][q] = '0'
                    if q - 1 >= 0 and grid[p][q-1] == '1' and (p, q-1) not in dq:
                        dq.append((p, q-1))
                        grid[p][q-1] = '0'
                    if q + 1 < c and grid[p][q+1] == '1' and (p, q+1) not in dq:
                        dq.append((p, q+1))
                        grid[p][q+1] = '0'
                    grid[p][q] = '0'
        return count
```