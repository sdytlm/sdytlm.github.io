/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void reorderList(ListNode head) {
        if(head==null || head.next==null) return ;
        
        // Find middle
        ListNode prev = new ListNode(-1);
        prev.next = head;
        ListNode p1 = prev;
        ListNode p2 = prev;
        while(p2!=null && p2.next!=null){
            p1 = p1.next;
            p2 = p2.next.next;
        }

        ListNode right = p1.next;
        ListNode left = head;
        p1.next = null;

        // Reverse the right list

        ListNode prevNode = right;
        ListNode nextNode = right.next;
        right.next = null;

        while(nextNode!=null){
            ListNode tmp = nextNode.next;
            nextNode.next = prevNode;
            prevNode = nextNode;
            nextNode = tmp;
        }
        right = prevNode;

        // Merge left and right
        while(right!=null){
            ListNode leftNext = left.next;
            ListNode rightNext = right.next;
            left.next = right;
            right.next = leftNext;
            left = leftNext;
            right = rightNext;
        
        }

    }
}
