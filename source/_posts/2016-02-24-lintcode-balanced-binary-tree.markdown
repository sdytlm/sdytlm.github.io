---
layout: post
title: "Balanced Binary Tree"
date: 2016-02-24
comments: true
categories: LintCode
tag: LintCode 
---

### Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

#### Example
Given binary tree A={3,9,20,#,#,15,7}, B={3,#,20,15,7}
```
A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.
```
<!--more-->
### Solution
* Time: O(n)
{% include_code LintCode/Balanced-Binary-Tree.py %}

