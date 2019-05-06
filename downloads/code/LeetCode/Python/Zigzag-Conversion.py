class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows <= 1 or numRows >=len(s):
            return s

        zigzag = ["" for i in range(numRows)]
        step = 1
        i = 0
        for c in s:
            zigzag[i] += c
            # 从0行开始的话往下走
            if i == 0:
                step = 1
            # 到达末尾行要返回
            if i == numRows -1:
                step = -1
            i += step
        ret = ""
        for i in zigzag:
            ret += i
        return ret
