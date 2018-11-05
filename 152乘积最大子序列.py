class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        localMax = nums[0]
        localMin = nums[0]
        maxProduct = nums[0]
        if len(nums) == 1: return nums[0]
        for i in range(1,len(nums)):
            if nums[i] >0:
                localMax = max(nums[i], localMax * nums[i])
                localMin = min(nums[i], localMin *nums[i])
            else:
                negativelocalMax = max(nums[i], localMin * nums[i])
                localMin = min(nums[i], localMax * nums[i])
                localMax = negativelocalMax
            maxProduct = max(maxProduct,localMax)
        return maxProduct