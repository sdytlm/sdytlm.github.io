---
layout: post
title: "Unique Binary Search Tree II"
date: 2016-07-03
comments: true
categories: LeetCode
tag: LeetCode
---


Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

#### Example
Given n = 3, your program should return all 5 unique BST's shown below.

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

<!--more-->
### Solution
* DFS search the left and right subtrees. Then merge the trees.
{% include_code LeetCode/Python/Unique-Binary-Search-Trees2.py %}
