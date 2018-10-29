class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        if len(set(nums)) == 1:
            return 2
        l = 0
        r = 1
        d = len(nums)
        while r < d:
            if nums[l] == nums[r]:
                r += 1
            elif nums[l] > nums[r]:
                n = 0
                for _ in range(l+1,r-1):
                    b = nums.pop(l)
                    nums += [b]
                    n += 1
                return r - n
            else:
                k = 0
                for _ in range(l+1,r-1):
                    a = nums.pop(l)
                    nums += [a]
                    k += 1
                l = r - k
                r = l + 1
        if l + 1 < r - 1:
            m = 0
            for _ in range(l+1, r-1):
                m += 1
            return r - m