class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import itertools
        a = list(range(1, n + 1))
        res = []
        for i in itertools.combinations(a, k):
            res.append(list(i))
        return res