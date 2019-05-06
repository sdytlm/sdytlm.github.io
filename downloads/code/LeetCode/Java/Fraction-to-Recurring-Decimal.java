public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
	if(numerator == 0) return "0";
	StringBuilder ret = new StringBuilder();
	// +/-
	ret.append((numerator>0) ^ (denominator>0)? "-" : "");
	long num = Math.abs((long)numerator);
	long den = Math.abs((long)denominator);

	// Integer part
	ret.append(num/den);
	num %= den;
	// no fractional part
	if(num==0) return ret.toString();

	// fractional part
	ret.append(".");
	// map<remainer, place you need to insert "(">
	HashMap<Long, Integer> map = new HashMap<Long, Integer>();
	map.put(num, ret.length());

	while(num!=0){
	    num *= 10;
	    ret.append(num/den);
	    num %= den;
	    if(map.containsKey(num)){
		// find repeating part
		int index = map.get(num);
		ret.insert(index, "(");
		ret.append(")");
		break;
	    }
	    else
		map.put(num,ret.length());
	}
	return ret.toString();
    }
}
