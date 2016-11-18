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
    // 必须要有两个global 变量
    int ret;
    int count;
    public int kthSmallest(TreeNode root, int k) {
        ret = 0;
        count = k;
        inorder(root);
        return ret;
        
    }
    public void inorder(TreeNode root){
        if(root.left!=null) 
            inorder(root.left);
        count--;
        if(count==0){
            ret = root.val;
            return ;
        }
        if (root.right!=null)  inorder(root.right);
        
    }
}
