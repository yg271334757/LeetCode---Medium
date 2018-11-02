class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        result = [1 for __ in range(n)]
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                result[i] = result[i-1] + 1
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                result[j] = max(result[j], result[j+1] + 1)
        return sum(result)