---
layout: post
title: "Binary Tree Level Order Traversal II"
date: 2016-08-22
comments: true
categories: LeetCode
tag: LeetCode
---

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

#### For example:
Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```

<!--more-->
### Solution
* BFS 然后翻转结果
{% include_code LeetCode/Python/Binary-Tree-Level-Order-Traversal2.py %}

* java solution: BFS, 需要stack辅助
{% include_code LeetCode/Java/Binary-Tree-Level-Order-Traversal2.java %}
