public class Solution {
    public int divide(int dividend, int divisor) {
	if(divisor==0 || (dividend == Integer.MIN_VALUE && divisor==-1))
	    return Integer.MAX_VALUE;
	int sign = (dividend > 0) ^ (divisor > 0) ? -1 : 1;
	long dvd = Math.abs((long)dividend);
	long dvs = Math.abs((long)divisor);
	int ret = 0;
	while(dvd >= dvs){
	    long tmp = dvs;
	    int multiple = 1;
	    while(dvd >= (tmp<<1)){
		tmp <<= 1;
		multiple <<= 1;
	    }
	    dvd -= tmp;
	    ret += multiple;
	}
	return sign==1? ret: -ret;
    }
}
