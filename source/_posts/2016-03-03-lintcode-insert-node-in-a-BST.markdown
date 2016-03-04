---
layout: post
title: "Insert Node in a Binary Search Tree"
date: 2016-03-02
comments: true
categories: LintCode
tag: LintCode 
---

Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

#### Example
Given binary search tree as follow, after Insert node 6, the tree should be:
```
  2             2
 / \           / \
1   4   -->   1   4
   /             / \ 
  3             3   6
```

<!--more-->
### Solution
* Time: O(n)
{% include_code LintCode/Insert-Node-in-a-BST.py %}
