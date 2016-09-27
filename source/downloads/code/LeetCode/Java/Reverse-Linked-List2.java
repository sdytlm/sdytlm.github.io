/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        // find prev;
        for(int i=1;i<m;i++)
            prev = prev.next;
        
        ListNode start = prev.next;
        ListNode then = start.next;

        for(int i=0;i<n-m;i++){
            start.next = then.next;
            then.next = prev.next;
            prev.next = then;
            then = start.next;
            
        }
        return dummy.next;
    }
}
