public class Solution {
    public int longestSubstring(String s, int k) {
        char[] str = s.toCharArray();
        return helper(str, 0, s.length(), k);    
    }

    int helper(char[] str, int start, int end, int k){
        if(end-start < k) return 0;
        // 记录每个字母出现的次数
        int[] count = new int[26];
        // 扫描str,记录每个字母出现的次数
        for(int i=start; i <end; i++)
            count[str[i]-'a']++;
    
        // Divde the str
        for(int i=0; i<26; i++){
            // str不包含i+'a'
            if(count[i]==0) continue;
            if(count[i]<k){
                for(int j = start; j < end; j++){
                    // 从ｊ这里分开
                    if(str[j] == i+'a')
                        return Math.max(helper(str, start,j,k), helper(str,j+1, end, k));
                
                }
            
            }
        }
        // 如果能到这里，说明str中所有的字母出现次数都至少是k
        return end-start;
    
    }
}
