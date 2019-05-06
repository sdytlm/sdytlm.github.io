public class Solution {
        public int[] twoSum(int[] numbers, int target) {
            int start = 0;
            int end = numbers.length-1;
            int[] ret = new int[2];
            while(start<end){
                int sum=numbers[start]+numbers[end];
                if(sum==target){
                    ret[0] = start+1;
                    ret[1] = end+1;
                    return ret;
                }
                else if(sum<target)
                    start++;
                else
                    end--;
            }
            return ret;
        }
}

