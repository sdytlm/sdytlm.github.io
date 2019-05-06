/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null || head.next==null) return head;
        // 找到中间点
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;
        while(fast!=null && fast.next!=null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        prev.next = null;

        // Divide
        ListNode left = sortList(head);
        ListNode right = sortList(slow);

        // Merge
        return merge(left,right);
    }

    ListNode merge(ListNode l1, ListNode l2){
        ListNode ret = new ListNode(0);
        ListNode cur = ret;
        while(l1!=null && l2!=null){
            if(l1.val < l2.val){
                cur.next = l1;
                l1 = l1.next;
            }
            else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
        if (l1!=null)
            cur.next = l1;

        if (l2!=null)
            cur.next = l2;
        
        return ret.next;
    }

}
