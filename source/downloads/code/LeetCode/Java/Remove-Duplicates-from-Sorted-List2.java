public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next==null) return head;
        ListNode newhead = new ListNode(-1);
        newhead.next = head;
        ListNode prev = newhead;
        ListNode cur = head;

        while(cur!=null){
            while(cur.next!=null && cur.next.val == cur.val)
                cur = cur.next;
            // 只有这种情况cur才会被真正加入newheadlist中
            if(prev.next == cur)
                prev = prev.next;
            else// 此时还无法判断cur.next是不是重复
                prev.next = cur.next;
            cur = cur.next;
            
        }
        return newhead.next;

    }
}
