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
    public int countNodes(TreeNode root) {
        if(root==null)
           return 0;
        int lh=0;int rh=0;
        TreeNode tmp = root;
        while(tmp){
            tmp = tmp.left;
            lh ++;
        }
        TreeNode tmp = root;
        while(tmp){
            tmp = tmp.right;
            rh++;
        }

        if(lh==rh)
            return Math.power(2,lh)-1;

        return countNodes(root.left)+countNodes(root.right)+1;
    }
}
