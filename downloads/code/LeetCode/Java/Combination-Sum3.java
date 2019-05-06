
public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
            List<List<Integer>> ret= new ArrayList<List<Integer>> ();
            List<Integer> tmp = new ArrayList<Integer>();
            dfs(ret, tmp, k, n, 1);
            return ret;
        }

    public void dfs(List<List<Integer>> ret, List<Integer> tmp, int k, int n, int start){
        if(n==0 && tmp.size() == k){
            List<Integer> li = new ArrayList<Integer>(tmp);
            ret.add(li);
            return;
        }
        for(int i=start; i<=9; i++){
            tmp.add(i);
            dfs(ret, tmp, k, n-i,i+1);
            tmp.remove(tmp.size()-1);
        }
       
    }
}

