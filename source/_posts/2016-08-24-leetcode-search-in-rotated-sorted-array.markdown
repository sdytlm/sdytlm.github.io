---
layout: post
title: "Search in Rotated Sorted Array"
date: 2016-08-24
comments: true
categories: leetcode
tag: leetcode
---


Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

<!--more-->
### Solution
* 二分查找
* 对于m来说，要么左面递增，要么右面递增，然后分别考虑target 在[l,m] 和 [m,r]中的情况

{% include_code LeetCode/Python/Search-in-Rotated-Sorted-Array.py %}
