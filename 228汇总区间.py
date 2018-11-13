class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        l = 0
        r = 1
        ans = []
        judge = [nums[l]]
        while r < len(nums):
            if nums[r] - nums[l] == 1:
                judge.append(nums[r])
            else:
                if len(judge) > 1:
                    ans.append('{0}->{1}'.format(judge[0], judge[-1]))
                elif len(judge) == 1:
                    ans.append(str(judge[0]))
                judge = [nums[r]]
            l = r 
            r += 1
        if len(judge) == 1:
            ans.append(str(judge[0]))
        elif len(judge) > 1:
            ans.append('{0}->{1}'.format(judge[0], judge[-1]))
        return ans