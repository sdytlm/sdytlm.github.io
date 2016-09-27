public class Solution {
    public String simplifyPath(String path) {
        Deque<String> stack = new LinkedList<String>();
 
        for (String s : path.split("/")){
            if(s.equals(".") || s.equals(""))
                continue;
            if(s.equals("..")){
                if(!stack.isEmpty())
                    stack.pop();
                continue;
            }
            
            stack.push(s);

        }
    // 生成字符串时要从stack的底部开始       
    String res = "";
    for (String dir : stack) res = "/" + dir + res;
    return res.isEmpty() ? "/" : res;
    }
}
