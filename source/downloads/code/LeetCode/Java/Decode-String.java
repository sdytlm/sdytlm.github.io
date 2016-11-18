public class Solution {
    public String decodeString(String s) {
        Stack<Integer> intStack = new Stack<Integer>();
        // current string
        StringBuilder cur = new StringBuilder();
        Stack<StringBuilder> strStack = new Stack<StringBuilder>();
        // current number
        int k = 0;
        for(char ch : s.toCharArray()){
            // 持续统计num
            if(Character.isDigit(ch)){
                k = k*10 + ch-'0';
            }
            else if (ch=='['){
                intStack.push(k);
                strStack.push(cur);

                // new cur and k
                cur = new StringBuilder();
                k = 0;
            }
            else if (ch == ']'){
                StringBuilder tmp = cur;
                cur = strStack.pop();
                // generate num*string
                for(k=intStack.pop();k>0;k--) cur.append(tmp);
            }
            // characters
            else cur.append(ch);
        
        }
        return cur.toString();
    }
}
