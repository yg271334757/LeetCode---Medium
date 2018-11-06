class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        substrings = {}
        for i in range(len(s) - 9):
            ss = s[i:i+10]
            if ss not in substrings:
                substrings[ss] = True
                
            elif substrings[ss]:
                result.append(ss)
                substrings[ss] = False
            
        return result