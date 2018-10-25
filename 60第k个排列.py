class Solution:
    def __init__(self):
        self.record = {} # n -> n!
    
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in range(1, n+1)]
        while n >= 1:
            num, k = k // self.factorial(n-1), k % self.factorial(n-1)
            if k > 0:
                res.append(str(nums[num]))
                nums.remove(nums[num])
            else:
                res.append(str(nums[num-1]))
                nums.remove(nums[num-1])

            n -= 1

        return ''.join(res)
    
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            if n in self.record:
                return self.record[n]
            else:
                res = n * self.factorial(n - 1)
                self.record[n] = res
                return res
        