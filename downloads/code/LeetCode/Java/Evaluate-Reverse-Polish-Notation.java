public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack<>();
        int a,b;
        for (String s : tokens){
            if (s.equals("+")){
                nums.push(nums.pop() + nums.pop());
            }
            else if (s.equals("*")){
                nums.push(nums.pop() * nums.pop());
            }
            else if (s.equals("/")){
                b = nums.pop();
                a = nums.pop();
                nums.push(a/b);
            }
            else if (s.equals("-")){
                b = nums.pop();
                a = nums.pop();
                nums.push(a-b);
            }
            else 
                nums.push(Integer.parseInt(s));
        
        }
        return nums.pop();
    }
}
