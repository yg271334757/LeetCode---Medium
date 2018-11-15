class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        i = 0
        j = n-1
        while i < j:
            mid = (i+j) / 2
            if citations[mid] == n-mid:
                return n-mid
            elif citations[mid] < n-mid:
                i = mid+1
            else:
                j = mid
        return min(citations[i],n-i)