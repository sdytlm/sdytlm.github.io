public class Solution {
    public List<Integer> majorityElement(int[] nums) {
       List<Integer> ret = new LinkedList<Integer>();
       int c1=0,c2=0,n1=0,n2=0;
       for (int num:nums){
            if(num==c1)
                n1++;
            else if(num==c2)
                n2++;
            else if(n1==0){
                c1 = num;
                n1++;
            }
            else if(n2==0){
                c2 = num;
                n2++;
            }
            else{
                n1--;
                n2--;
            }         
       }
       int count1 = 0;
       int count2 = 0;
       for(int num: nums){
            if(num==c1)
                count1++;
            // must be else if [0,0,0]
            else if(num==c2)
                count2++;
       }
       if(count1>nums.length/3)
           ret.add(c1);
       if(count2>nums.length/3)
           ret.add(c2);
        
        return ret; 
    }
}
