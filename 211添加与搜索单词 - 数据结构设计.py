import collections
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = collections.defaultdict(set)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        l = len(word)
        self.words[l].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        import re
        l = len(word)
        if '.' not in word:
            return word in self.words[l]
        for i in self.words[l]:
            if re.match(word, i) and l == len(i):
                return True
        return False