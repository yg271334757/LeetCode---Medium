# LeetCode---Medium
LeetCode---Medium
#### No. 3.  使用栈的方法
#### No. 31. 原来函数还可以这样用
#### No. 36. 创建二维数组： a = [[[0] for _ in range(3)] for _ in range(3)]
#### No. 39. DFS
<<<<<<< HEAD
             ```
=======
             '''
>>>>>>> f056e1012ab6ef236ca205d65699abe76081bd08
             def dfs(remain, stack):
            if not remain:
                res.append(stack)
                return 
            for item in candidates:
                if item > remain:
                    break
                elif not stack or item >= stack[-1]:
                    dfs(remain - item, stack + [item])
<<<<<<< HEAD
            ```
=======
            '''
>>>>>>> f056e1012ab6ef236ca205d65699abe76081bd08
