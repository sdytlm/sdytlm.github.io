---
layout: post
title: "Majority Element"
date: 2016-07-01
comments: true
categories: LeetCode
tag: LeetCode
---


Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

<!--more-->

### Solution:
维护一个当前的候选众数e 和一个初始为0的计数器 count。遍历数组时，我们看当前的元素x:

*  如果计数器是0, 我们将候选众数置为 x 并将计数器置为 1
*  elif e==x, count++,
*  else count--

{% include_code LeetCode/Python/Majority-Element.py %}
