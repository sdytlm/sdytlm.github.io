public class Solution {
    List<List<String>> resultLst;
    ArrayList<String> currLst;

    public List<List<String>> partition(String s) {
        resultLst = new ArrayList<List<String>>();
        currLst = new ArrayList<String>();
        dfs(s,0);
        return resultLst;        
        }
    
    // DFS
    public void dfs(String s, int l){
        if (currLst.size()>0 && l>=s.length()){
            List<String> r = (ArrayList<String>) currLst.clone();
            resultLst.add(r);
        }
        for (int i=l;i<s.length();i++){
            if(isPalindrome(s,l,i)){
                currLst.add(s.substring(l,i+1));
                dfs(s,i+1);
                currLst.remove(currLst.size()-1);
            }
        }
    }

    public boolean isPalindrome(String s, int i, int j){
        if (i > j) return false;
        while (i<j){
            if (s.charAt(i) != s.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }
}


