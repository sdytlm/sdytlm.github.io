class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ####
        # transitionTable[state][inputtype] = value
        ####

        # state: 0==invalid, 1==space, 2==sign, 3==digit, 4==dot, 5==exponent, 6==num_inputs
        # inputtype: 如下
        INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5
        # value:
        # 0 no input or just spaces
        # 1 input is digits
        # 2 no digits in front just Dot
        # 3 sign
        # 4 digits and dot in front
        # 5 input e or E (exponent)
        # 6 after e input sign
        # 7 after e input digits
        # after valid input input space
        state=0; i=0
        while i<len(s):
            inputtype = INVALID
            if s[i]==' ': inputtype=SPACE
            elif s[i]=='-' or s[i]=='+': inputtype=SIGN
            elif s[i] in '0123456789': inputtype=DIGIT
            elif s[i]=='.': inputtype=DOT
            elif s[i]=='e' or s[i]=='E': inputtype=EXPONENT
            
            state=transitionTable[state][inputtype]
            if state==-1: return False
            else: i+=1
        return state == 1 or state == 4 or state == 7 or state == 8
