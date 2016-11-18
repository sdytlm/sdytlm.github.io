public class Solution {
    public NestedInteger deserialize(String s) {
    
        if(s.isEmpty()) return null;
        // 只有一个int string -> int
        if(s.charAt(0) != '[') return new NestedInteger(Integer.valueOf(s));

        Stack<NestedInteger> stack = new Stack<NestedInteger>();
        NestedInteger cur = null;
        int l = 0;

        for(int r=0; r<s.length(); r++){
            char ch = s.charAt(r);
            // 把当前cur压入栈，并开始一个新的
            if(ch == '['){
                if(cur != null)
                    stack.push(cur);
                cur = new NestedInteger();
                l = r+1;
            }
            // 结束当前NestedInteger，弹出一个
            else if (ch==']'){
                String num = s.substring(l,r);
                if(!num.isEmpty()) cur.add(new NestedInteger(Integer.valueOf(num)));

                if(!stack.isEmpty()){
                    NestedInteger top = stack.pop();
                    top.add(cur);
                    cur = top;
                }
                l = r+1;
            }
            // 向cur中插入一个新num
            else if (ch==','){
                // 有数字
                if(s.charAt(r-1)!=']'){
                    String num = s.substring(l,r);
                    cur.add(new NestedInteger(Integer.valueOf(num)));
                }
                l = r+1;
            
            }
        
        }    
        return cur;
    }
}
