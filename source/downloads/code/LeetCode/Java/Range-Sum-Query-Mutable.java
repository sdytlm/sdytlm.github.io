public class NumArray {
    // class: SegmentTreeNode
    class SegmentTreeNode {
	int start, end;
	SegmentTreeNode left, right;
	// <left, right> segments
	int sum;
	// sum of values in <left, right> segments

	public SegmentTreeNode(int start, int end){
	    this.start = start;
	    this.end = end;
	    this.left = null;
	    this.right = null;
	    this.sum = 0;
	}
    }

    SegmentTreeNode root = null;
    public NumArray(int[] nums) {
	root = buildTree(nums, 0, nums.length-1);
    }

    // buildTree(...):
    private SegmentTreeNode buildTree(int[] nums, int start, int end){
	if(start > end) return null;
	SegmentTreeNode ret = new SegmentTreeNode(start, end);
	if(start==end) ret.sum = nums[start];
	else{
	    // binary recursive 
	    int mid = start + (end-start)/2;
	    ret.left = buildTree(nums,start,mid);
	    ret.right = buildTree(nums,mid+1,end);
	    ret.sum = ret.left.sum+ret.right.sum;
	}
	return ret;
    }

    public void update(int i, int val) {
	update(root,i,val);
    }

    // update(...)
    public void update(SegmentTreeNode root, int pos, int val){
	if(root.start==root.end){
	    root.sum = val;
	    return;
	}
	// binary search
	int mid = root.start + (root.end-root.start)/2;
	if(pos <= mid)
	    update(root.left, pos, val);
	else
	    update(root.right, pos, val);
	root.sum = root.left.sum + root.right.sum;
    }

    public int sumRange(int i, int j) {
	return sumRange(root,i,j);
    }

    // sumRange(...)
    public int sumRange(SegmentTreeNode root, int start, int end){
	if(root.start==start && root.end==end) return root.sum;
	int mid = root.start+(root.end-root.start)/2;
	if(end<=mid)
	    // <start, end> in left tree
	    return sumRange(root.left, start, end);
	else if (start>=mid+1)
	    // <start, end> in right tree
	    return sumRange(root.right, start, end);
	else
	    // start in left tree, end in right tree
	    return sumRange(root.left, start,mid) + sumRange(root.right, mid+1, end);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
