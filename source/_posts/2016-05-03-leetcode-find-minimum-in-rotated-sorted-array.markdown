---
layout: post
title: "Find Minimum in Rotated Sorted Array"
date: 2016-05-03
comments: true
categories: LeetCode
tag: LeetCode
---

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

<!--more-->

### Solution
* Binary Search
* Split the array into two parts, then recursively binary search each part.

{% include_code LeetCode/Python/Find-Minimum-in-Rotated-Sorted-Array.py %}
