public class Solution {
    public int myAtoi(String str) {
        // empty
        if (str.length()==0)
            return 0;
        // space
        str = str.trim();

        // sign
        int sign = 1;
        int index = 0;
        // case: "+1"
        if (str.charAt(index)=='-' || str.charAt(index)=='+'){
            sign = str.charAt(index)=='+'?1:-1;
            index++;
        }

        // convert str to int
        int num = 0;
        while(index<str.length()){
            int digit = str.charAt(index)-'0';
            if (digit < 0 || digit > 9)
                break;
            // 判断越界问题
            if (Integer.MAX_VALUE/10 < num || (Integer.MAX_VALUE/10==num && Integer.MAX_VALUE%10<digit))
                return sign==1?Integer.MAX_VALUE:Integer.MIN_VALUE;

            num = num*10 +digit;
            index++;
        }
        return sign*num;
                        
    }
}
