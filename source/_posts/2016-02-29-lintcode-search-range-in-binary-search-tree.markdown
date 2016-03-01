---
layout: post
title: "Search Range in Binary-Search-Tree"
date: 2016-02-29
comments: true
categories: LintCode
tag: LintCode 
---

`Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.`

#### Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

```
        20
   /  \
  8   22
 / \
4   12

```

<!--more-->
### Solution

* Time: O(n)
{% include_code LintCode/Search-Range-in-Binary-Search-Tree.py %}
