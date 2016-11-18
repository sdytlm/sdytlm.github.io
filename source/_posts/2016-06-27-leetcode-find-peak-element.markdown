---
layout: post
title: "Find Peak Element"
date: 2016-06-27
comments: true
categories: LeetCode
tag: LeetCode
---

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

#### Example
in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


#### Note:
Your solution should be in logarithmic complexity.

<!--more-->
### Solution
* Java: iteration+recursive
{% include_code LeetCode/Java/Find-Peak-Element.java %}

* Python
{% include_code LeetCode/Python/Find-Peak-Element.py %}
