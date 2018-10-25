class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for d in path.split('/'):
            if d == '..' and len(stack) > 0:
                stack.pop()
            if d not in ('','.','..'):
                stack.append(d)
        return '/'+'/'.join(stack)