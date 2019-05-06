public class Solution {
    public List<String> findItinerary(String[][] tickets) {
        Map<String, PriorityQueue<String>> targets = new HashMap<>();
        for (String[] ticket : tickets)
            // 若ticket[0]在map, 则在他的priorityqueue中加入ticket[1], 否则创建一个priorityqueue.
            targets.computeIfAbsent(ticket[0], k -> new PriorityQueue()).add(ticket[1]);
        List<String> route = new LinkedList();
        Stack<String> stack = new Stack<>();
        stack.push("JFK");
        while(!stack.empty()){
            String cur = stack.peek();
            // 若cur在targets中，并且他的priorityqueue不为空，则把他priority中所有元素全部插入
            while(targets.containsKey(stack.peek()) && !targets.get(stack.peek()).isEmpty())
                stack.push(targets.get(stack.peek()).poll());
            route.add(0,stack.pop());
        }
        return route;

    }
}
