public class Solution {
    public String multiply(String num1, String num2) {
        int l1 = num1.length();
        int l2 = num2.length();
        int[] pos = new int[l1+l2];
        for(int i=l1-1; i>=0; i--){
            for(int j=l2-1; j>=0; j--){
                int mul = (num1.charAt(i)-'0')*(num2.charAt(j)-'0');
                int pos1 = i+j;
                int pos2 = i+j+1;
                // 要考虑之前的进位
                int sum = mul+pos[pos2];
                
                pos[pos1] += sum/10;
                pos[pos2] = sum%10;
            
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<pos.length;i++){
            // 如果sb为空，并且pos[i]是０，则不插入,case: "0"
            if(pos[i] == 0 && sb.length()==0) continue;
            sb.append(pos[i]);
        }
        return sb.length()==0? "0" : sb.toString();

    }
}
