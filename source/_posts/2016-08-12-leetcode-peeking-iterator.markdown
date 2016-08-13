---
layout: post
title: "Peeking Iterator"
date: 2016-08-12
comments: true
categories: LeetCode
tag: LeetCode
---


Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

#### Hint:

* Think of "looking ahead". You want to cache the next element.
* Is one variable sufficient? Why or why not?
* Test your design with call order of peek() before next() vs next() before peek().
* For a clean implementation, check out Google's guava library source code.

<!--more-->
### Solution
* 难点在于如何得到当前iterator指向的val, 因为我们只有next函数可以调用
* 在初始化时候运行一下next()

{% include_code LeetCode/Python/Peeking-Iterator.py %}
