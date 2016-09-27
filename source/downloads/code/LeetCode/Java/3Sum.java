public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ret = new LinkedList<List<Integer>>();
        if (nums.length == 0)
            return ret;
        //　排序
        Arrays.sort(nums);
        
        for (int i=0;i<nums.length-2;i++){
            if(i==0 || nums[i] != nums[i-1]){
                int l = i+1;
                int r = nums.length-1;
                while (l<r){
                    int sums = nums[i]+nums[l]+nums[r];
                    if (sums==0){
                        // asList: array->list
                        ret.add(Arrays.asList(nums[i],nums[l],nums[r]));
                        while(l<r && nums[l]==nums[l+1]) l++;
                        while(l<r && nums[r]==nums[r-1]) r--;
                        l++;
                        r--;
                    }
                    else if(sums<0)
                        l ++;
                    else
                        r--;
                }
            }
        }
        return ret;
    }
}
