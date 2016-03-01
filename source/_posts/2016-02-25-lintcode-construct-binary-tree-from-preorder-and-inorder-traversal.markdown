---
layout: post
title: "Construct Binary Tree from Preorder and Inorder Tranversal"
date: 2016-02-25
comments: true
categories: LintCode
tag: LintCode 
---

`Given preorder and inorder traversal of a tree, construct the binary tree.`

#### Example
Given in-order [1,2,3] and pre-order [2,1,3], return a tree:

```
  2
 / \
1   3
```

#### Note
You may assume that duplicates do not exist in the tree.

<!--more-->
### Solution

* Time:O(n)
* Find each `root` in preorder list
* split the inorder list by the `root`
* recursive func parameters is preorder[left_p,right_p], inorder[left_p,right_p]
* use hash map to reduce the time to find `root` index in inorder list.

{% include_code LintCode/Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.py %}
