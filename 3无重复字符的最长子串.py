class Solution:
    def lengthOfLongestSubstring(self, s):
        if s:
            arr = []
            res = 0
            for i in s:
                while i in arr:
                    arr.pop(0)
                arr.append(i)
                cur = len(arr)
                if cur > res:
                    res = cur
            return res
        else:
            return 0