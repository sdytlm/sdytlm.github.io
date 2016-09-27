public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> ret = new LinkedList<String>();
        dfs(ret, s, "", 0 ,0);
        return ret; 
    }
    public void dfs(List<String> ret, String s, String sol, int index, int len){
        if (index == s.length() && len == 4){
            ret.add(sol);
            return;
        }
        if (len == 4 || index > s.length())
            return;

        for (int l = 1; l<4; l++){
            if(index+l > s.length())
                return;
            String sub = s.substring(index, index+l);
            if ((sub.startsWith("0") && sub.length()>1) || (l==3 && Integer.parseInt(sub)>=256)) 
                continue;
            dfs(ret, s, sol+sub+(len==3?"":"."), index+l, len+1);
        }
    }
}
