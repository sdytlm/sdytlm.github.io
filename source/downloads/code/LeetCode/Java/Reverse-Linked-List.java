/**
 * Definition for singly-linked list.
 * public class ListNode {
 *      int val;
 *      ListNode next;
 *      ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        return reverse(head,null);           
    }

    public ListNode reverse(ListNode head, ListNode newhead){
        if(head==null)
            return newhead;
        ListNode nextNode = head.next;
        head.next = newhead;
        return reverse(nextNode,head);
        
    }
}
