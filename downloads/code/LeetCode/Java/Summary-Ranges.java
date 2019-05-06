public class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> list = new ArrayList();
        if(nums.length==1){
            list.add(nums[0]+"");
            return list;
        }
        for(int i=0;i<nums.length;i++){
            int cur = nums[i];
            while(i+1<nums.length && nums[i]+1 == nums[i+1])
                i++;
            if(cur!=nums[i])
                list.add(cur+"->"+nums[i]);
            else
                list.add(cur+"");
        }
        return list;
    }
} 