public class Solution {
    public boolean canPartition(int[] nums) {
        HashMap<Integer, Integer> hash_map = new HashMap<Integer, Integer>();
        int sum = 0;
        for(int num: nums){
            if(hash_map.containsKey(num))
                hash_map.put(num, hash_map.get(num)+1);
            else
                hash_map.put(num,1);
            sum += num;
        } 
        if(sum%2 !=0) return false;
        return helper(hash_map, sum/2);      
    }

    // dfs
    public boolean helper(HashMap<Integer, Integer> hash_map, int target){
        if(hash_map.containsKey(target) && hash_map.get(target) > 0) return true;
        for(int num: hash_map.keySet()){
            if(num < target && hash_map.get(num) > 0){
                hash_map.put(num, hash_map.get(num)-1);
                if(helper(hash_map, target-num)) return true;
                hash_map.put(num, hash_map.get(num)+1);
            }
        }
        return false;
    }
}
