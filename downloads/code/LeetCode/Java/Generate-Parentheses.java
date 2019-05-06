public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ret = new LinkedList<String>();    
        dfs(ret,"",0,0,n);
        return ret;
    }

    public void dfs(List<String> ret, String tmp, int l, int r, int max){
            if(tmp.length() == 2*max){
                ret.add(tmp);
                return;
            }
            if(l<max)
                dfs(ret, tmp+'(', l+1, r, max);
            if(r<l)
                dfs(ret, tmp+')', l, r+1, max);
    }
}
