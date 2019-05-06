public class Solution {
    public void sortColors(int[] nums) {
        if(nums == null || nums.length==0)
            return;
        int red = 0;
        int blue = nums.length-1;
        
        int i=0;
        while(i<=blue){
            if(nums[i]==0){
                swap(nums,red,i);
                red++;
                i++;
            }
            else if (nums[i]==2){
                swap(nums,blue,i);
                blue--;
            }
            else
                i++;
        }
        return ; 

    }

    public void swap(int[] nums, int a, int b){
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}
