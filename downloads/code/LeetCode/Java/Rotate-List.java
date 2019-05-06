/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        ListNode prev = new ListNode(-1);
        prev.next = head;
        ListNode cur = prev;
        int i=0;
        int n =0;
        // get n
        while(cur!=null){
            n++;
            cur = cur.next;
        }
        // get new head
        cur = prev;
        while(i<n){
            cur = cur.next;
        }
        prev.next = cur.next;
        cur.next = null;

        return prev.next;
    }
}
