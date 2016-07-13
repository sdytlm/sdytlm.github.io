---
layout: post
title: "Binary Search Tree Iterator"
date: 2016-07-05
comments: true
categories: LeetCode
tag: LeetCode
---

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

#### Note: 
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

<!--more-->
### Solution
* 维护一个栈，从根节点开始，每次迭代地将根节点的左孩子压入栈，直到左孩子为空为止。

* 调用next()方法时，弹出栈顶，如果被弹出的元素拥有右孩子，则以右孩子为根，将其左孩子迭代压栈。

{% include_code LeetCode/Python/Binary-Search-Tree-Iterator.py %}
