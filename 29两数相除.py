class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a = int(str(dividend / divisor).split('.')[0])
        if -2147483648 <= a <= 2147483647:
            return a
        elif a < -2147483647:
            return -2147483648
        else:
            return 2147483647