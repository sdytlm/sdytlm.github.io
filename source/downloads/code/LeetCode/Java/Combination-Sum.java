public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> tmp = new ArrayList<Integer>();
        Arrays.sort(candidates);
        dfs(ret, tmp, candidates, target, 0);
        return ret;        
    }

    void dfs(List<List<Integer>> ret, List<Integer> tmp, int[] candidates, int target, int start){
        if(target==0)
            ret.add(new ArrayList<Integer>(tmp));
        else if (target>0){
            for(int i= start; i < candidates.length; i++){
                tmp.add(candidates[i]);
                dfs(ret, tmp, candidates, target-candidates[i], i);
                tmp.remove(tmp.size()-1);
            }
        }
    }
}
