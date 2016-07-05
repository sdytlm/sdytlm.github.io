---
layout: post
title: "3Sum Closest"
date: 2016-07-01
comments: true
categories: LeetCode
tag: LeetCode
---

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#### Example
Given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

<!--more-->
### Solution
* 3 level loops
* 内2层循环根据sum和target的关系移动

{% include_code LeetCode/Python/3Sum-Closet.py %}
