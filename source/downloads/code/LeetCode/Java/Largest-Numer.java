public class Solution {
    public String largestNumber(int[] nums) {
        if(nums==null || nums.length==0) return "";
	// convert int array to string array
	String[] s_nums = new String[nums.length];
	for(int i=0; i<nums.length; i++)
	    s_nums[i] = String.valueOf(nums[i]);

	// Comparator for sort
	Comparator<String> comp = new Comparator<String>(){
	    @Override
	    public int compare(String s1, String s2){
	        String a = s1+s2;
		String b = s2+s1;
		// reverse order
		return b.compareTo(a);
	    }
	    };
	Arrays.sort(s_nums, comp);
	// Corner case: only a bunch of "0"
	if(s_nums[0].charAt(0)=='0') return "0";

	StringBuilder sb = new StringBuilder();
	for(String s : s_nums)
	    sb.append(s);
	return sb.toString();
    }
}
