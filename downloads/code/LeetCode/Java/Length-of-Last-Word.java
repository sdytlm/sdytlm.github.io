public class Solution {
    public int lengthOfLastWord(String s) {
        if (s.length()==0)
            return 0;
        // 去掉首尾空格
        s = s.trim();
        int lastIndex = s.lastIndexOf(' ')+1;
        return s.length()-lastIndex;
    }
}
