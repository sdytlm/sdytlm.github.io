---
layout: post
title: "Binary Tree Postorder Traversal"
date: 2016-08-23
comments: true
categories: LeetCode
tag: LeetCode
---


Given a binary tree, return the postorder traversal of its nodes' values.

#### For example:
```
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
```
return [3,2,1].

#### Note: 
Recursive solution is trivial, could you do it iteratively?

<!--more-->
### Solution
* 维护两个堆栈，一个记录结果，一个正常遍历数组，

{% include_code LeetCode/Python/Binary-Tree-Postorder-Traversal.py %}
