from collections import deque
class Solution:
    def calculate(self, s):
        s = s.replace(' ','')
        nums = deque([])
        i, l = 0, len(s)
        def num(x):
            if s[x] in '0123456789':
                j = 1
                num = s[x]
                while x + j < l:
                    if s[x+j] not in '+-*/':
                        num += s[x+j]
                        j += 1
                    else:
                        break
            return int(num)
        while i < l:
            if s[i] in '0123456789':
                a = num(i)
                nums.append(a)
                i += len(str(a))
            elif s[i] == '*':
                b = nums.pop()
                c = num(i+1)
                nums.append(b * c)
                i += len(str(c))+1
            elif s[i] == '/':
                d = nums.pop()
                e = num(i+1)
                if d > 0:
                    nums.append(d // e)
                else:
                    nums.append(-((-d) // e))
                i += len(str(e))+1
            elif s[i] == '+':
                f = num(i+1)
                nums.append(f)
                i += len(str(f))+1
            else:
                g = num(i+1)
                nums.append(-g)
                i += len(str(g))+1
        return sum(nums)