---
layout: post
title: "Unique Binary Search Trees"
date: 2016-01-13
comments: true
categories: LintCode
tag: LintCode
---
### Unique Binary Search Trees
Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

#### Example
Given n = 3, there are a total of 5 unique BST's.
```
1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3
```
<!--more-->
### Solution
* Time: O(n^2)
* count[n]: how many BST trees for n
* count[0] = 1
* count[1] = 1
* count[2] = count[0] * count[1] + count[1] * count[0]
* count[3] = count[0] * count[2] + count[1] * count[1] + count[2] * count[0]
> count[n] = sum(count[i] * count[n-1-i]) i in [0,n-1]

{% include_code LintCode/Unique-Binary-Search-Trees.py %}
