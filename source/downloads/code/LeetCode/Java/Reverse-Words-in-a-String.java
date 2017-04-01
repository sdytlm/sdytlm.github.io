public class Solution {
    public String reverseWords(String s) {
	String[] parts = s.trim().split("\\s+");
	String ret = "";
	for(int i=parts.length-1; i>0; i--){
	    ret += parts[i]+" ";
	}
	return ret+parts[0];
    }
}
