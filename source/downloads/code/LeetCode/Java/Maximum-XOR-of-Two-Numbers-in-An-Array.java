public class Solution {
    public int findMaximumXOR(int[] nums) {
        int max = 0;
        int mask = 0;
        for (int i=31; i>=0 i--){
            // 看看有没有第i位不同的num
            Set<Integer> map = new HashSet<Integer>();
            mask = mask | (1<<i);
           
            for(int num : nums)
                map.add(num & mask);

            // 若第i位有不同的num, 更新max
            int tmp = max | (1<<i);
            for (int prefix : set){
                if(set.contains(tmp ^ prefix)){
                    max = tmp;
                    break;
                }
            }
        
        }
        return max;
    }
}
