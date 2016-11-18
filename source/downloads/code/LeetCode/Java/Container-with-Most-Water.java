public class Solution {
    public int maxArea(int[] height) {
        int water = 0;
        int left = 0;
        int right = height.length-1;
        while(left<right){
            int h = Math.min(height[left], height[right]);
            water = Math.max(water, h*(right-left));
            while (height[left] <= h && left<right) left++;
            while (height[right] <= h && left<right) right--;

        }        
        return water;
    }
}
