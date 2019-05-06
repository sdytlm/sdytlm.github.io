public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        // <freq, nums[i]->nums[j]->nums[...]>
        List<Integer>[] bucket = new List[nums.length+1];
        // <num[i], freq>
        Map<Integer, Integer> freqMap = new HashMap<Integer, Integer>();
        for (int num: nums){
            freqMap.put(num, freqMap.getOrDefault(num,0)+1);
        }
        for (int key: freqMap.keySet()){
            int freq = freqMap.get(key);
            if(bucket[freq]==null)
                bucket[freq] = new LinkedList<Integer>();
            bucket[freq].add(key);
        }

        List<Integer> ret = new LinkedList<Integer>();
        for(int pos = bucket.length-1; pos>=0 && ret.size() < k; pos--){
            if(bucket[pos]!=null){
                ret.addAll(bucket[pos]);
            }
        }
        return ret;
    }

}
