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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ret = new LinkedList<Integer>();
        if(root==null)
            return ret;
        Stack<TreeNode> rights = new Stack<TreeNode>();
        
        while(root!=null){
            ret.add(root.val);
            if(root.right!=null)
                rights.push(root.right);
            
            root = root.left;
            if (root==null && !rights.isEmpty())
                root = rights.pop();
        } 
        return ret;   
    }
}
