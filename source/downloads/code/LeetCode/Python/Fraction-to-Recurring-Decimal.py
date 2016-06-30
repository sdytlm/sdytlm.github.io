class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator:
            return "0"
        ret = ""
        if numerator < 0 or denominator < 0:
            ret = "-"
        if numerator <0 and denominator < 0:
            ret = ""
        
        p = abs(numerator)
        d = abs(denominator)

        ret += str(p/d)
        if p%d == 0:
            return ret
        else:
            ret += "."
        index = 0
        # hash[remain:index of frac]
        hash = dict()
        frac = ""

        # 22/7
        if p > d:
            p = p-d*(p/d)
        
        # get fraction part
        while p%d not in hash:
            remain = p%d
            if remain == 0:
                break
            # 1/3
            if p < d:
                p = 10*p
            frac += str(p/d)
            p = p-d*(p/d)
            hash[remain] = index
            index += 1
        # p can divide d
        if p%d == 0:
            return ret+frac
        
        startindex = hash[p%d]
        return ret+frac[0:startindex]+"("+frac[startindex:index]+")"

