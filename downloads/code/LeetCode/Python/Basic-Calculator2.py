### This solution will Timeout
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        seq = re.split('(\D)',s)
        operator = []
        nums = []
        stack = []
        i = 0

        while i < len(seq):
            if seq[i] == " ":
                i += 1
                continue
            # number
            if seq[i] not in "+-*/":
                stack.append(int(seq[i]))
                i += 1

            # operator: */ will handle the calculation here
            if seq[i] in "*/":
                left = stack.pop()
                right = int(seq[i+1])
                if seq[i] == "*":
                    ret = left*right
                else:
                    ret = left / right
                stack.append(ret)
                i += 2
            else:
                # "+-"
                stack.append(seq[i])
                i += 1
        # handle +- here
        while len(stack) > 1:
            left = stack.pop(0)
            op = stack.pop(0)
            right = stack.pop(0)

            if op == "+":
                stack.insert(left+right)
            else:
                stack.insert(left-right)

        return stack[0]




class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(r'\d+', ' \g<0> ', s)
        seq = s.split()

        idx = 0
        total = 0
        d = 0
        last_op = "+"
        while idx < len(seq):
            
            # numbers
            if seq[idx] not in "*/+-":
                d = int(seq[idx])
            # calculate "*" and "/" immediately
            if seq[idx] in "*/":
                if seq[idx] == "*":
                    d = d*int(seq[idx+1])
                if seq[idx] == "/":
                    d = d/int(seq[idx+1])
                idx += 1
            # only interest in last_op
            if seq[idx] in "+-":
                if last_op == "+":
                    total += d
                if last_op == "-":
                    total -= d
                last_op = seq[idx]
            idx += 1

        if last_op == "+":
            return total+d
        else:
            return total-d
