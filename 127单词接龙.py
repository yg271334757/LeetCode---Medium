class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        headQ = set([beginWord])
        tailQ = set([endWord])
        step = 1

        if endWord not in wordSet:
            return 0
        else:
            wordSet.discard(endWord)

        while headQ:
            step += 1
            currSet = set()
            for word in headQ:
                for i in range(len(word)):
                    p1 = word[:i]
                    p2 = word[i + 1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new = p1 + c + p2
                        if new in tailQ:
                            return step
                        if new in wordSet:
                            currSet.add(new)
                            wordSet.remove(new)

            headQ = currSet
            if len(headQ) > len(tailQ):
                headQ, tailQ = tailQ, headQ

        return 0
        