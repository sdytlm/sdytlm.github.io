public class Solution {
    public String convert(String s, int numRows) {
        char[] c = s.toCharArray();
        int len = c.length;
        StringBuffer[] sb = new StringBuffer[numRows];
        for (int i=0;i<numRows;i++)
            sb[i] = new StringBuffer();
        int i =0;
        while(i<len){
            for(int idx = 0; idx<numRows && i<len; idx++)
                sb[idx].append(c[i++]);
            for(int idx = numRows-2; idx>=1 && i<len; idx--)
                sb[idx].append(c[i++]);
        }

        for(i=1;i<numRows;i++)
            sb[0].append(sb[i]);
        return sb[0].toString();
    }
}
