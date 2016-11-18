/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        if(root==null)
            return ;
        
        TreeLinkNode cur = null;
        TreeLinkNode prev = root;
        while(prev.left != null){
            cur = prev;
            // 没一层都连起来
            while(cur!=null){
                cur.left.next = cur.right;
                if(cur.next!=null)
                    cur.right.next = cur.next.left;
                cur = cur.next;
            }

            // 下一层
            prev = prev.left;
        
        }   
    
    }
}
