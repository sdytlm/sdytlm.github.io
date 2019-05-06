public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ret = new LinkedList<List<Integer>> ();
        List<Integer> tmp = new LinkedList<Integer>();

        dfs(ret, tmp, 1, k, n); 
        return ret;       
    }

    public void dfs(List<List<Integer>> ret, List<Integer> tmp, int start, int k, int n){
        if(tmp.size() == k){
            ret.add(new LinkedList(tmp));
            return;
        }
        for(int i=start;i<=n;i++){
            tmp.add(i);
            dfs(ret, tmp, i+1,k,n);
            tmp.remove(tmp.size()-1);
        }
    }
}

