/**
 * definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> ret = new LinkedList<String>();
        if (root==null)
            return ret;
        searchBT(root,""+root.val,ret);
        return ret;    
    }

    public void searchBT(TreeNode node, String path, List<String> ret){
        if (node.left==null && node.right == null)
            ret.add(path);
        if (node.left != null)
            searchBT(node.left, path+"->"+node.left.val, ret);
        if (node.right != null)
            searchBT(node.right, path+"->"+node.right.val, ret);

    }
}
