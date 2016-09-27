public class Solution {
    public boolean containsDuplicate(int[] nums) {
        final Set<Integer> distinct = new HashSet<Integer>();
        for (int num : nums){
            if(!distinct.add(num))
                return true;
        }
        return false;
    }
}
