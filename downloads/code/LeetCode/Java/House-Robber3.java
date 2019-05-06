/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int rob(TreeNode root) {
        if(root==null) return 0;
        int[] ret = dfs(root);    
        return Math.max(ret[0],ret[1]);
    }

    public int[] dfs(TreeNode node){
        // ret[0]: rob, ret[1]: non-rob
        int[] ret = new int[2];
        
        if(node==null){
            ret[0] = 0;
            ret[1] = 0;
            return ret;
        }

        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        ret[0] = left[1]+right[1]+node.val;
        ret[1] = Math.max(left[0],left[1])+Math.max(right[1],right[0]);

        return ret;
    }

}
