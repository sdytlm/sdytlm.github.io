public class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        hm.put('M',1000);
        hm.put('D',500);
        hm.put('C',100);
        hm.put('L',50);
        hm.put('X',10);
        hm.put('V',5);
        hm.put('I',1);
        int ret = 0;
        for(int i=0;i<s.length()-1;i++){
            if(hm.get(s.charAt(i))<hm.get(s.charAt(i+1)))
                ret -= hm.get(s.charAt(i));
            else
                ret += hm.get(s.charAt(i));
        }
        return ret+hm.get(s.charAt(s.length()-1));        
    }
}


