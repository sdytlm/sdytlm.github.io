/*
 *  Definition for a binary tree node.
 *  public class TreeNode {
 *      int val;
 *      TreeNode left;
 *      TreeNode right;
 *      TreeNode(int x) { val = x; }
 *      }
 */
public class Solution {
        public List<Integer> rightSideView(TreeNode root) {
            List<Integer> ret = new LinkedList<Integer>();
            if(root==null)
                return ret;
            helper(ret, root, 0);
            return ret;
        }

        public void helper(List<Integer> ret, TreeNode node, int depth){
            if(node == null)
                return ;
            if(depth == ret.size()){
                ret.add(node.val);
            }

            helper(ret, node.right, depth+1);
            helper(ret, node.left, depth+1);
        
        }
}
