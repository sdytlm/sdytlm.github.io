public class Solution {
    public int lengthLongestPath(String input) {
        // 把输入按照\n分开
        String[] parts = input.split("\n");
        
        int[] stack = new int[parts.length+1];
        //stack[i]: 坐标为i的"\t"对应的路径长度
        int maxLen = 0;
        for(String s : parts){
            // lev: 当前s到最后一个\t的长度
            int lev = s.lastIndexOf("\t")+1;
            int curLen = stack[lev+1] = stack[lev]+s.length()-lev+1;
            if(s.contains(".")) maxLen = Math.max(maxLen, curLen-1);
        }
        return maxLen;
    }
}
