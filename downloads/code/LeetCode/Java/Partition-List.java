/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode less = new ListNode(Integer.MAX_VALUE);
        ListNode nLess  = new ListNode(Integer.MIN_VALUE);
        ListNode ret = less;
        ListNode nLessHead = nLess;
        
        while(head!=null){
            ListNode nextNode = head.next;
            head.next = null;
            if(head.val < x){
                less.next = head;
                less = less.next;
            }
            else{
                nLess.next = head;
                nLess = nLess.next;
            }
            head = nextNode;
        }
        less.next = nLessHead.next;
        return ret.next;
        
    }
}
