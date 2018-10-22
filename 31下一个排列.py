class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if sorted(nums) == list(reversed(nums)):
            nums.sort()
            return
        i = len(nums) - 1
        while i >= 1:
            if nums[i] > nums[i-1]:
                break
            i -= 1
        pos = i-1
        j = i
        while j < len(nums):
            if nums[j] <= nums[pos]:
                nums[pos], nums[j-1] = nums[j-1], nums[pos]
                break
            elif j == len(nums) - 1:
                nums[pos], nums[j] = nums[j], nums[pos]
                break
            j += 1
        l = i
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1