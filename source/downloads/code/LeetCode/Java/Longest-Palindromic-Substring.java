public class Solution {
    private int lo;
    private int maxLen;
 
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2) return s;

        for(int i=0; i<len-1; i++){
            // 奇数长度
            extentPalindrome(s, i, i);
            // 偶数长度
            extentPalindrome(s, i, i+1);
        }
        return s.substring(lo, lo+maxLen);
    }
    
    public void extentPalindrome(String s, int start, int end){
        // start, end　之间一定维持着palindrome
        while(start >=0 && end < s.length() && s.charAt(start) == s.charAt(end)){
            // 持续向两面扩张
            start--;
            end++;
        }
    
        // 注意: 此时end,start已经过了
        if(maxLen < end-start-1){
            maxLen = end-start-1;
            lo = start+1;
        }
    }
}
