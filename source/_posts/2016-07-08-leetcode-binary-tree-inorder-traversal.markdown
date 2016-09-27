---
layout: post
title: "Binary Tree Inorder Traversal"
date: 2016-07-08
comments: true
categories: LeetCode
tag: LeetCode
---



Given a binary tree, return the inorder traversal of its nodes' values.

#### Example:
Given binary tree [1,null,2,3],

```
   1
    \
     2
    /
   3
```

return [1,3,2].

#### Note: 
Recursive solution is trivial, could you do it iteratively?

<!--more-->
### Solution
* Iterative solution
{% include_code LeetCode/Python/Binary-Tree-Inorder-Traversal.py %}

* 更简练的java solution: 不需要预处理左字树
{% include_code LeetCode/Java/Binary-Tree-Inorder-Traversal.java %}


