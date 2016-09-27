---
layout: post
title: "Invert Binary Tree"
date: 2016-05-23
comments: true
categories: LeetCode
tag: LeetCode
---

Invert a binary tree.


#### Example
```
         4
   /   \
  2     7
 / \   / \
1   3 6   9
```
to

```
         4
   /   \
  7     2
 / \   / \
9   6 3   1

```

<!--more-->
### Solution

{% include_code LeetCode/Python/Invert-Binary-Tree.py %}

* Java solution: recursive. 也可以用stack

{% include_code LeetCode/Java/Invert-Binary-Tree.java %}
