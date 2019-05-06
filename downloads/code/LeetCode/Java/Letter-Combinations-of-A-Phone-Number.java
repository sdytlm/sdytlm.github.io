public class Solution {
    public List<String> letterCombinations(String digits) {
        LinkedList<String> ret = new LinkedList<String>();
        String[] mapping = new String[]{"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        if(digits.length()==0) return ret;
        ret.add("");
        for(int i=0;i<digits.length();i++){
            // x 是在mapping中的索引
            int x = Character.getNumericValue(digits.charAt(i));
            // ret 中peek 长度如果和i相等，则制造下一个digit
            while(ret.peek().length()==i){
                // remove peek element
                String top = ret.remove();
                for(char s : mapping[x].toCharArray())
                    ret.add(top+s);
            }
            
            
        } 
        return ret;   
    }
}
