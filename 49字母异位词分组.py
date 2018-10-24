class Solution:
    def groupAnagrams(self,strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strdict = {}
        for letter in strs:
            mark = sorted(letter)
            if tuple(mark) in strdict:
                strdict[tuple(mark)] += [letter]
            else:
                strdict[tuple(mark)] = [letter]
        return list(strdict.values())