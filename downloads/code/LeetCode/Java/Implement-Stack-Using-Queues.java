class MyStack {
    Queue<Integer> myQueue;
    public MyStack(){
        this.myQueue = new LinkedList<Integer>();
    }
    // Push element x onto stack.
    public void push(int x) {
        myQueue.add(x);
        //　把queue反过来
        // add: 插入到队尾
        // poll(): 弹出head
        for (int i = 1; i<myQueue.size(); i++){
            myQueue.add(myQueue.poll());
        }
    }

    // Removes the element on top of the stack.
    public void pop() {
        myQueue.poll();
    }

    // Get the top element.
    public int top() {
        return myQueue.peek();
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return myQueue.isEmpty();
    }
}
