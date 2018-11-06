class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = n
        while res > m:
            res = res & (res - 1)
        return res