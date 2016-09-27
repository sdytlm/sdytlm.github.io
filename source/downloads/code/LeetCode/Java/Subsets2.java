public class Solution {
    List<List<Integer>> ret = new ArrayList<List<Integer>> ();
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        if (nums==null || nums.length==0)
            return ret;
        Arrays.sort(nums);
        // add [] into result
        result.add(new ArrayList<Integer>());
        int begin = 0;
        for(int i = 0; i < nums.length; i++){
                // find non-duplicate
                if (i==0 || nums[i] != nums[i-1])
                    begin = 0;
                int size = result.size();
                for (int j=begin; j<size; j++){
                    List<Integer> cur = new ArrayList<Integer>(result.get(j));
                    cur.add(nums[i]);
                    result(cur);
                }
                begin = size;
        }
        
        return ret;
    }
}

