---
layout: post
title: "Kth Smallest Element in A BST"
date: 2016-07-06
comments: true
categories: LeetCode
tag: LeetCode
---


Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

#### Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

#### Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

* Try to utilize the property of a BST.
* What if you could modify the BST node's structure?
* The optimal runtime complexity is O(height of BST).

<!--more-->
### Solution
* Mantain a stack to record the left subtree of current node.
{% include_code LeetCode/Python/Kth-Smallest-Element-in-A-BST.py %}
