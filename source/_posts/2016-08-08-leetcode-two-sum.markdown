---
layout: post
title: "Two Sum"
date: 2016-08-08
comments: true
categories: LeetCode
tag: LeetCode
---

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

#### Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

<!--more-->
### Solution
* 不要一上来把hash_map填满，不需要nums排序
{% include_code LeetCode/Python/Two-Sum.py %}
