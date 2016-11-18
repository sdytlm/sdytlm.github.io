public class Solution {
        public int lengthOfLongestSubstring(String s) {
            if(s.length()==0) return 0;
            HashMap<Character, Integer> map = new HashMap<Character, Integer>();
            int ret = 0;
            // 不重复子字符串的起点
	    int j=0;
            for(int i=0; i<s.length();i++){
               if(map.containsKey(s.charAt(i)))
                   j = Math.max(j, map.get(s.charAt(i))+1);
               map.put(s.charAt(i),i);
               ret = Math.max(ret, i-j+1);
            }            
            return ret;
        }
}
