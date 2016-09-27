---
layout: post
title: "Min Stack"
date: 2016-06-01
comments: true
categories: LeetCode
tag: LeetCode
---

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.

#### Example
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

<!--more-->
### Solution

* Java: One Stack
{% include_code LeetCode/Java/Min-Stack.java %}

* Python: Two stack
{% include_code LeetCode/Python/Min-Stack.py %}
