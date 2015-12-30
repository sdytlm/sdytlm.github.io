---
layout: post
title: "Search for A Range"
date: 2015-12-29
comments: true
categories: LintCode
tag: LintCode
---

### Search for a Range

Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

#### Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

#### Challenge
O(log n) time.

<!--more-->

### Solution

* Time: O(logn): Space O(1)
* Binary search for two times in order to get index1, index2
{% include_code LintCode/Search-for-A-Range.py %}
