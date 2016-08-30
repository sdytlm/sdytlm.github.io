---
layout: post
title: "Recover Binary Search Tree"
date: 2016-08-30
comments: true
categories: leetcode
tag: leetcode
---



Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

#### Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

<!--more-->

### Solution
* 中序遍历应该返回递增序列
* 若非叶子节点与叶子搞错了，则会出现一个递减序列 (self.prev, self.n1)
* 若非叶子与非叶子搞错了，则出现２个递减序列(self.n1, self.n2)

{% include_code LeetCode/Python/Recover-Binary-Search-Tree.py %}
