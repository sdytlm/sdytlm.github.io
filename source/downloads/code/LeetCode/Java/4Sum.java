public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if(nums.length < 4) return ret;
        Arrays.sort(nums);
        int n = nums.length;
        for(int i=0;i<n-3;i++){
            // skip 重复nums[i]
            if(i>0 && nums[i] == nums[i-1]) continue;
            for(int j=i+1;j<n-2;j++){
               // skip重复的nums[j]
               if(j>i+1 && nums[j] == nums[j-1]) continue;
               int low = j+1;
               int high = n-1;

               // j, low, high　组成3sum
                while (low<high){
                    int sum = nums[i]+nums[j]+nums[low]+nums[high];
                    if(sum==target){
                        ret.add(Arrays.asList(nums[i],nums[j],nums[low],nums[high]));
                        //skip 重复的nums[low] nums[high]
                        while(low<high && nums[low] == nums[low+1]) low++;
                        while(low<high && nums[high] == nums[high-1]) high--;
                        low++;
                        high--;
                    }
                    else if(sum < target) low++;
                    else    high--;
                
                }
            
            
            }
        
        
        
        }
        return ret;
    }
}
