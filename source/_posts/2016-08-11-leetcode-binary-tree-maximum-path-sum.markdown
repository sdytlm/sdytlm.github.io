---
layout: post
title: "Binary Tree Maximum Path Sum"
date: 2016-08-11
comments: true
categories: LeetCode
tag: LeetCode
---

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

#### Example:
Given the below binary tree,

```
       1
      / \
     2   3
```
Return 6.

<!--more-->
### Solution
* DFS，注意节点可能是负值

{% include_code LeetCode/Python/Binary-Tree-Maximum-Path-Sum.py %}
