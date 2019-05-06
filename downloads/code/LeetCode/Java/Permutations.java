public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> l0 = new ArrayList<Integer>();
        if(nums==null || nums.length==0)
            return ret;
        l0.add(nums[0]);
        ret.add(l0);

        for(int i=1;i<nums.length;i++){
            List<List<Integer>> new_ret = new ArrayList<List<Integer>>();
            // j: new pos
            for(int j=0;j<=i;j++){
                // each list in ret
                for(List<Integer>l: ret){
                    // copy list
                    List<Integer> new_l = new ArrayList<Integer>(l);
                    new_l.add(j,nums[i]);
                    new_ret.add(new_l);
                }
            }
            ret = new_ret;
        }

        return ret;
    }
}
