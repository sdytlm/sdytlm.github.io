---
layout: post
title: "Binary Tree Level Order Traversal"
date: 2016-02-26
comments: true
categories: LintCode
tag: LintCode 
---

`Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).`

#### Example
Given binary tree {3,9,20,#,#,15,7},

```
        3
   / \
  9  20
        /  \
      15   7
``` 
return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

#### Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use DFS algorithm to do it.

<!--more-->

### Solution
* Time O(n)
* Count the queue.size() in the beginging of iteration, that is the num of nodes in each level.

{% include_code LintCode/Binary-Tree-Level-Order-Traversal.py %}
