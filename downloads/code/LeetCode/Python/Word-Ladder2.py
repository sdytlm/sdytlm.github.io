class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # 把结尾单词插入list中
        wordlist.add(endWord)
        # BFS 每一层节点和他们的parents 
        level = set([beginWord])

        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(word)):
                        newWord = word[:i]+c+word[i+1:]
                        # 找到新单词
                        if newWord in wordlist and newWord not in parents:
                            # word 是 word的parents
                            next_level[newWord].add(word)
            level = next_level
            parents.update(next_level)

        # 从end word 开始建立结果
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

