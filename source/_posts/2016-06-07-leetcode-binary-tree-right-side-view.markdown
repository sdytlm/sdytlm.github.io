---
layout: post
title: "Binary Tree Right Side View"
date: 2016-06-07
comments: true
categories: LeetCode
tag: LeetCode
---

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#### Example
Given the following binary tree,
```
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
```

<!--more-->
### Solution
* BFS
{% include_code LeetCode/Python/Binary-Tree-Right-Side-View.py %}
