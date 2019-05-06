public class Solution {
    private long getID(long i, long w){
	// in Java, -3/5 = 0
	return i < 0 ? (i+1)/w-1 : i/w;
    }
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
	if (k<1 || t<0) return false;
	Map<Long, Long> map = new HashMap<>();
	long w = (long)t+1;
	for(int i=0; i < nums.length; i++){
	    long m = getID(nums[i],w);
	    if(map.containsKey(m))
		return true;
	    if(map.containsKey(m-1) && Math.abs(nums[i]-map.get(m-1))<w)
		return true;
	    if(map.containsKey(m+1) && Math.abs(nums[i]-map.get(m+1))<w)
	        return true;
	    map.put(m, (long)nums[i]);
	    if(i>=k) map.remove(getID(nums[i-k], w)); // only keep k elements in map
	}
	return false;
    }
}
