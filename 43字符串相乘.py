class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        numdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        def str2num(x):
            x = x[-1::-1]
            num = 0
            for i in range(len(x)):
                num += numdict[x[i]] * 10 ** i
            return num
        return str(str2num(num1) * str2num(num2))