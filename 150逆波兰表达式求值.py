class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        number = []
        res = 0
        for i in tokens:
            if i not in '+-*/':
                number.append(int(i))
            else:
                b = number.pop()
                a = number.pop()
                if i == '+':
                    res = int(a + b)
                    number.append(res)
                elif i == '-':
                    res = int(a - b)
                    number.append(res)
                elif i == '*':
                    res = int(a * b)
                    number.append(res)
                else:
                    res = int(a / b)
                    number.append(res)
        return res