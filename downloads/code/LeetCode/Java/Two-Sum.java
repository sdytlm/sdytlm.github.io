public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for (int i=0; i<nums.length;i++){
            if(map.containsKey(target-nums[i])){
                int[] ret = {map.get(target-nums[i]), i};
                return ret;
            }
            map.put(nums[i],i);
        }
        return null;
    }
}
