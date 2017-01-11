public class Solution {
    public boolean isAdditiveNumber(String num) {
        int l = num.length();
        
        // 第一个数的长度不能超过L的一半,i 是第一个数的长度
        // 第一个数: nums[0,i]
        for (int i=1;i<=(l-1)/2;i++){
            // 每一个数，如果长度>=2, 则不能以０开始
            if(num.charAt(0)=='0' && i>=2) break;
            
            // 第二个数:nums[i,j]
            for(int j=i+1; l-j>=j-i && l-j>=i; j++){
                if(num.charAt(i)=='0' && j-i>=2) break;
                // 第一个数和第二个数
                long num1 = Long.parseLong(num.substring(0,i));
                long num2 = Long.parseLong(num.substring(i,j));
                // num剩余部分
                String remain = num.substring(j);
                // check 是不是additive
                if(isAdditive(remain, num1, num2)) return true;
            }
        
        }
        return false;        
    }
    public boolean isAdditive(String str, long num1, long num2){
        // 若剩余为空，则成立
        if(str.equals("")) return true;

        long sum = num1+num2;
        // sum的String版本是s
        String s = ((Long)sum).toString();
        // 若str不是以s开始，则不成立
        if(!str.startsWith(s)) return false;
        // sum是第二个，num2变成第一个; 
        return isAdditive(str.substring(s.length()), num2, sum);
        
    }

}
