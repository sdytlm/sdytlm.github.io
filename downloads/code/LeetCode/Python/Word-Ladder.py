class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        alpha = "abcdefghijklmnopqrstuvwxyz"
        n = len(beginWord)
        stack = []
        stack.append([beginWord,1])
        wordList.add(endWord)
        while stack:
            tmp = stack.pop(0)
            word = tmp[0]
            val = tmp[1]
            alpha = "abcdefghijklmnopqrstuvwxyz"
            if word == endWord:
                return val

            for i in range(len(word)):
                for j in alpha:
                    if j == word[i]:
                        continue
                    newWord = word[:i]+j+word[i+1:]
                    if newWord in wordList:
                        stack.append([newWord,val+1])
                        wordList.remove(newWord)
        return 0
