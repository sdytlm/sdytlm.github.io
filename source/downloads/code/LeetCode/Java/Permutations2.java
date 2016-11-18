public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ret = new LinkedList<List<Integer>>();
        if(nums==null || nums.length==0) return ret;
        List<Integer> tmp = new LinkedList<Integer>();
        boolean[] used = new boolean[nums.length];
        Arrays.sort(nums);
        dfs(ret,nums,used,tmp);
        return ret;
    }

    public void dfs(List<List<Integer>> ret, int[] nums, boolean[] used, List<Integer> tmp){
        if(tmp.size()==nums.length){
            ret.add(new ArrayList<Integer>(tmp));
            return;
        }
        for(int i=0;i<nums.length;i++){
            if(used[i]) continue;
            // used[i-1]若在tmp中，不能continue
            if(i>0 && nums[i-1]==nums[i] && !used[i-1]) continue;
            used[i] = true;
            tmp.add(nums[i]);
            dfs(ret, nums, used, tmp);
            used[i] = false;
            tmp.remove(tmp.size()-1);
        
        }
    }
}
