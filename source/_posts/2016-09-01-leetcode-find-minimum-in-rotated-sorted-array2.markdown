---
layout: post
title: "Find Minimum in Rotated Sorted Array II"
date: 2016-09-01
comments: true
categories: LeetCode
tag: LeetCode
---

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

<!--more-->
### Solution
* 改良的二分
{% include_code LeetCode/Python/Find-Minimum-in-Rotated-Sorted-Array2.py %}
