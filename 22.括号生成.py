def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    results = []
    
    def dfs(path="", left=n, right=n):
        if left == 0 and right == 0:
            return results.append(path)
        elif left == right:
            dfs(path+"(", left-1, right)
        elif left < right:
            if left > 0: dfs(path+"(", left-1, right)
            if right > 0: dfs(path+")", left, right-1)
    
    dfs()
    return results