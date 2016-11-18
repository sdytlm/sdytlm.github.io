
public class Solution {
    public int calculate(String s) {
        if(s==null || s.length()==0) return 0;
        int len = s.length();
        Stack<Integer> stack = new Stack<Integer>();
        int num = 0;
        char ops = '+';
        for(int i=0;i<len;i++){
            // number
            if(Character.isDigit(s.charAt(i))){
                num = num*10 + s.charAt(i)-'0';
            }
            // ops: 我们使用的是上一次的ops
            if((!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ') || i==len-1){
                if(ops == '+')
                    stack.push(num);
                if(ops == '-')
                    stack.push(-num);
                if(ops == '*')
                    stack.push(stack.pop()*num);
                if(ops == '/')
                    stack.push(stack.pop()/num);
                ops = s.charAt(i);
                num = 0;

            }
        }    
        int ret = 0;
        for(int i: stack)
            ret+=i;
        return ret;    
    }
}

