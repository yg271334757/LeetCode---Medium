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