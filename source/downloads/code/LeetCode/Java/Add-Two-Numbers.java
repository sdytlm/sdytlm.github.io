/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode(-1);
        ListNode tmp = ret;
        int sum = 0;
        
        while(l1!=null || l2!=null){
            sum /= 10;
            if(l1 != null){
                sum += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                sum += l2.val;
                l2 = l2.next;
            }
            tmp.next = new ListNode(sum%10);
            tmp = tmp.next;
        
        } 
        if(sum >=10)
            tmp.next = new ListNode(1);
        return ret.next;       
    }
}
