public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> tmp = new ArrayList<Integer>();

        Arrays.sort(nums);
        dfs(ret, tmp, nums, 0);

        return ret;  
    }


    public void dfs(List<List<Integer>> ret, List<Integer> tmp, int[] nums, int index){
        
        ret.add(new ArrayList<Integer>(tmp));
        
        for(int i=index; i < nums.length; i++){
            tmp.add(nums[i]);
            dfs(ret, tmp, nums, i+1);
            tmp.remove(tmp.size()-1);
        }

    }
}
