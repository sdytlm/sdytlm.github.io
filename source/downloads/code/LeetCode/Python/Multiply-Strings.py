# Sol1: TLE on large int
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        mid_result = []
        # calculate each digit of num2 * num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        for i in num2:
            carry = 0
            result = ""
            for j in num1:
                val = int(i)*int(j)+carry
                carry = val / 10
                result = str(val%10)+result
            if carry != 0:
                result = str(carry)+result
            mid_result.append(result[:])

        n = len(mid_result)
        result = mid_result[0]
        for i in range(1,n):
            result = self.add_string(result,mid_result[i]+"0"*i)
        return result
            
    def add_string(self,s1,s2):
        i=len(s1)-1
        j=len(s2)-1
        carry = 0
        ret = ""
        while i>=0 or j>=0:
            if i >=0 and j >= 0:
                val = int(s1[i])+int(s2[j])+carry
                i -= 1
                j -= 1
            elif i>=0:
                val = int(s1[i])+carry
                i -= 1
            else: #j>=0:
                val = int(s2[j])+carry
                j -= 1

            carry = val/10
            ret = str(val%10)+ret
           
        if carry != 0:
            ret = str(carry)+ret
        return ret

# Sol2
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = num1[::-1]; num2 = num2[::-1]
        arr = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])
        ans = []
        for i in range(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] / 10
            if i < len(arr)-1:
                arr[i+1] += carry
            ans.insert(0, str(digit))
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        return ''.join(ans)



if __name__ == "__main__":
    sol = Solution()
    print sol.multiply("98","9")
