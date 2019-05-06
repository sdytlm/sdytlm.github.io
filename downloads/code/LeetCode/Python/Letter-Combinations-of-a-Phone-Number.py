class Solution(object):
    tel = {"0":" ", "1": "", "2":"abc", "3":"def", "4":"ghi", "5":"jkl",
     "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    def tel_comb(self,digits,ret,vector):
        if digits:
            codes = self.tel[digits[0]]
            for i in codes:
                self.tel_comb(digits[1:],ret,vector+i)
        else:
            if vector not in ret:
                ret.append(vector[:])

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if digits == None or digits == "":
            return ret
        self.tel_comb(digits,ret,"")
        return ret
