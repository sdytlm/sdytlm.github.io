---
layout: post
title: "Search for a Range"
date: 2016-08-07
comments: true
categories: LeetCode
tag: LeetCode
---

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

#### Example
Given [5, 7, 7, 8, 8, 10] and target value 8,

return [3, 4].

<!--more-->
### Solution
* Java: 两次二分
{% include_code LeetCode/Java/Search-for-A-Range.java %}


* Python: Binary Search

{% include_code LeetCode/Python/Search-for-a-Range.py %}

