/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null)
            return head;
        ListNode prev = head;
        ListNode nextNode = prev.next;
        while (nextNode != null){
            while (nextNode != null && nextNode.val == prev.val)
                nextNode = nextNode.next;
            prev.next = nextNode;
            prev = prev.next;
        }
        return head;  
    }
}
