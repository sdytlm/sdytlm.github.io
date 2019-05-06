public class Solution {
    public int characterReplacement(String s, int k) {
        int start = 0;
        int max_char_nums = 0;
        int[] count = new int[128];
        for(int end = 0; end<s.length(); end++){
            max_char_nums = Math.max(max_char_nums,++count[s.charAt(end)]);
            // 窗口右移
            if(max_char_nums+k<=end-start)
                count[s.charAt(start++)]--;
        }
        return s.length()-start;
    }
}
