class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        # 把s1,s2转换成数组
        l1 = list(s1)
        l2 = list(s2)
        l1 = sorted(l1)
        l2 = sorted(l2)
        
        if l1 != l2:
            return False
        
        length = len(l1)
        for i in range(1,length):
            # 没有交换s11==s21 and s12==s22
            if self.isScramble(s1[i:],s2[i:]) and self.isScramble(s1[:i],s2[:i]):
                return True
            # 有交换 s11==s22 and s12 == s21
            if self.isScramble(s1[i:],s2[:length-i]) and self.isScramble(s1[:i], s2[length-i:]):
                return True
        return False
