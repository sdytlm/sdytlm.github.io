---
layout: post
title: "Merge Intervals"
date: 2016-08-23
comments: true
categories: LeetCode
tag: LeetCode
---

Given a collection of intervals, merge all overlapping intervals.

#### For example,
Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

<!--more-->
### Solution
* 按照start 排序
* 然后有重叠时修改ret[-1].end 
{% include_code LeetCode/Python/Merge-Intervals.py %}
