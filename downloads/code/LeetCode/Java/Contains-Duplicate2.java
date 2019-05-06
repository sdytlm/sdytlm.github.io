public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> hash_map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (hash_map.containsKey(nums[i])){
                if (i-hash_map.get(nums[i]) <= k) return true;
            }
            // 若nums[i]存在,但是i-hash_map.get(nums[i])>k, 也要更新hash_map            
            hash_map.put(nums[i],i);
        }
        return false;     
    }
}
