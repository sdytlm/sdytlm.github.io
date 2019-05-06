/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode prev = new ListNode(Integer.MIN_VALUE);
        while(head != null){
            ListNode nextNode = head.next;
            head.next = null;
            // find pos
            ListNode tmp = prev;
            while(tmp.next!=null && tmp.next.val < head.val)
                tmp = tmp.next;
            
            head.next = tmp.next;
            tmp.next = head;

            head = nextNode;
        }
        return prev.next;
    }
}
