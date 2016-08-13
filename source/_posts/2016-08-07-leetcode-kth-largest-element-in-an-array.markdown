---
layout: post
title: "Kth Largest Element in an Array"
date: 2016-08-07
comments: true
categories: LeetCode
tag: LeetCode
---

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

#### Example
Given [3,2,1,5,6,4] and k = 2, return 5.

#### Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


<!--more-->

### Solution
* Sort: O(nlogn)
* Quick Select: O(n)
{% include_code LeetCode/Python/Kth-Largest-Element-in-an-Array.py %}
