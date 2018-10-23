# LeetCode---Medium
LeetCode---Medium
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
<<<<<<< HEAD
                if c >= 1 and x[c] == x[c - 1]: #去除重复的元素
=======
                if c >= 1 and x[c] == x[c - 1]:
>>>>>>> 67f293aed4eea6e361a4f1c13030cf892200efba
                    continue
                if remain - i == 0:
                    res.append(stack+[i])
                    break
                elif remain - i < 0:
                    break
                else:
                    dfs(x[c+1:], remain - i, stack + [i])
```