/**
 * Definition for a binary tree node.
 *  public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
       if(inorder.length==0 || postorder.length==0 || inorder.length!=postorder.length) return null;
       HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
       for(int i=0;i<inorder.length;i++)
           map.put(inorder[i],i);
        return helper(inorder, postorder, map, 0, inorder.length-1, 0, postorder.length-1);

    }
    public TreeNode helper(int[] inorder, int[] postorder, Map<Integer, Integer> map, int in_start, int in_end, int po_start, int po_end){
       if(in_start>in_end || po_start>po_end) return null;
       TreeNode root = new TreeNode(postorder[po_end]);
       int in_index = map.get(postorder[po_end]);
       root.left = helper(inorder, postorder, map, in_start,in_index-1,po_start, po_start+in_index-in_start-1);
       root.right = helper(inorder, postorder, map, in_index+1, in_end, po_start+in_index-in_start, po_end-1);
     return root;  
    
    }
}
