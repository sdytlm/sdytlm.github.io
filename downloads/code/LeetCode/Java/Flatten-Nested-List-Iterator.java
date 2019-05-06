public class NestedIterator implements Iterator<Integer> {
    Stack<NestedInteger> stack = new Stack<>(); 
    public NestedIterator(List<NestedInteger> nestedList) {
        for(int i=nestedList.size()-1; i>=0; i--)
            stack.push(nestedList.get(i));
        
    }

    @Override
    public Integer next() {
        return stack.pop().getInteger();
    }

    @Override
    public boolean hasNext() {
        while(!stack.isEmpty())
        {
            NestedInteger cur = stack.peek();
            if(cur.isInteger()) return true;
            stack.pop();
            for(int j=cur.getList().size()-1; j>=0; j--)
                stack.push(cur.getList().get(j));
        }
        return false;
    }
}
