class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        elements = [0] * len(words)
        for i,s in enumerate(words):
            for c in s:
                elements[i] |= 1<<(ord(c)-97)
        ret = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (elements[i] & elements[j]):
                    ret = max(ret, len(words[i])*len(words[j]))     
        return ret
