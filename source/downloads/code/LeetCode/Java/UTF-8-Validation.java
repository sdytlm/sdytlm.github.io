public class Solution {
    public boolean validUtf8(int[] data) {
        int cnt = 0;
        for(int d : data){
            // 第一个utf8字段
            if(cnt == 0){
                if((d>>5) == 6) cnt = 1; // 110
                else if ((d>>4) == 14) cnt = 2;  // 1110
                else if ((d>>3) == 30) cnt = 3;  // 11110
                else if ((d>>7) return false;   // 不是正确的标识字节
        
            } else{// 后续字段
                if((d>>6)!=2) return false;     // 10
                cnt--;
            }
        
        }
        return cnt==0;        
    }
}
