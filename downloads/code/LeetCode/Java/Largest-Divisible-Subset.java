public class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        int n = nums.length;
        // parent[i] = j 记录nums中第i个元素是第j个元素为最大元素的集合扩展得到的
        int[] parent = new int[n];
        // dp[i]; 最大元素是nums[i]的LDS集合包含多少元素
        int[] dp = new int[n];        
        Arrays.sort(nums);
        // lds集合中最大的元素的下标
        int max_index = 0;
        // lds集合的数量
        int max_num = 0;

        for(int i=nums.length-1; i>=0; i--){
        
            for(int j=i; j<nums.length;j++){
                if(nums[j] % nums[i] == 0 && dp[i] < 1+dp[j]){
                    dp[i] = 1+dp[j];
                    parent[i] = j;
                
                    if(dp[i] > max_num){
                        max_num = dp[i];
                        max_index = i;
                    }
                
                }
                    
            
            }
        
        }

        List<Integer> ret = new ArrayList();
        for(int i=0; i<max_num; i++){
            ret.add(nums[max_index]);
            max_index = parent[max_index];
        }
        return ret;

    }
}
