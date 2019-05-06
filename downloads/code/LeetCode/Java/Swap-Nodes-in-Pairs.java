/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(-1);
        ListNode prev = dummy;
        prev.next = head;
        if(head==null || head.next==null)
            return head;
        
        while (prev.next!=null && prev.next.next!=null){
            ListNode first = prev.next;
            ListNode second = prev.next.next;
    
            first.next = second.next;        
            prev.next = second;
            prev.next.next = first;
            
            prev = prev.next.next;
            
        }
        return dummy.next;
    }
}
