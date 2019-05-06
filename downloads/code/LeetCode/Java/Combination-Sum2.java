public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ret = new ArrayList<List<Integer>> ();
        List<Integer> tmp = new ArrayList<Integer>();
        dfs(ret, tmp, candidates, target, 0);
        return ret;
    }

    public void dfs(List<List<Integer>> ret, List<Integer> tmp, int[] candidates, int target, int index){
        if(target==0){
            ret.add(new ArrayList<Integer>(tmp));
            return;
        }
        if(target<0) return;

        for(int i=index;i<candidates.length;i++){
            if(i>index && candidates[i]==candidates[i-1]) continue;
            tmp.add(candidates[i]);
            dfs(ret, tmp, candidates, target-candidates[i], i+1);
            tmp.remove(tmp.size()-1);
        
        }
    }
}
