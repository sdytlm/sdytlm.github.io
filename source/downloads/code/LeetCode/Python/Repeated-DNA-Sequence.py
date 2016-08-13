class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        if not s:
            return ret
        # use 2 bits to represent DNA, We just need 20bit to represent a 10-letter DNA
        dna = {'A':0,'C':1,'G':2,'T':3}
        hash_map = dict()
        
        sum = 0
        for x in range(len(s)):
            sum = ((sum<<2) + dna[s[x]]) & 0xFFFFF # 20bit
            if x< 9:
                continue

            hash_map[sum] = hash_map.get(sum, 0) + 1
            if hash_map[sum] ==2:
                ret.append(s[x-9:x+1])
        return ret
