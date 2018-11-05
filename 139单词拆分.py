class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # # Solution 1
        dp = [False for i in range(len(s)+1)] # dp[i] means wordBreak(s[:i],wordDict)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i)[::-1]:
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]