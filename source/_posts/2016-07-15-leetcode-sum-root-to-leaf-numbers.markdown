---
layout: post
title: "Sum Roof to Leaf Numbers"
date: 2016-07-15
comments: true
categories: LeetCode
tag: LeetCode
---


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

### Example

```
        1
   / \
  2   3
```
The root-to-leaf path 1->2 represents the number 12.

The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

<!--more-->
### Solution
* Recursive
* Java
{% include_code LeetCode/Java/Sum-Root-to-Leaf-Numbers.java %}


* Tranverse the tree and record the value for each path
{% include_code LeetCode/Python/Sum-Root-to-Leaf-Numbers.py %}
