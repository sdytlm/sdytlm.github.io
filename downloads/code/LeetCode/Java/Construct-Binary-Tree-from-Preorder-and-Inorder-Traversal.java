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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int n = preorder.length;
        if (n==0)
            return null;
        return helper(preorder, 0, inorder, 0, n-1);
            
    }

    public TreeNode helper(int[] preorder,int ps,int[] inorder, int is, int ie){
        if(ps > preorder.length-1 || is > ie)
            return null;
        TreeNode node = new TreeNode(preorder[ps]);
        // find preorder[ps] in inorder: 左子树的长度
        int index=0;
        for(index=is; index<=ie;index++){
            if(inorder[index]==preorder[ps])
                break;
        }
        
        node.left = helper(preorder, ps+1,inorder,is,index-1);
        node.right = helper(preorder, ps+1+index-is,inorder,index+1, ie);
        return node; 
    
    } 
}
