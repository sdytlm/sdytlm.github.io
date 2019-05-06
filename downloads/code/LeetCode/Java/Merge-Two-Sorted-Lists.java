/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode root = new ListNode(-1);
        ListNode ret = root;
        while(l1!=null && l2!=null){
            if(l1.val<=l2.val){
                root.next = l1;
                l1 = l1.next;
            }
            else{
                root.next = l2;
                l2 = l2.next;
            }
            root = root.next;
        }    
        while(l1!=null){
            root.next = l1;
            root = root.next;
            l1 = l1.next;
        }
        while(l2!=null){
            root.next = l2;
            root = root.next;
            l2 = l2.next;
        }
        return ret.next;
    }

}
