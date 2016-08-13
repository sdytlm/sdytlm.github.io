---
layout: post
title: "First Missing Positive"
date: 2016-08-11
comments: true
categories: LeetCode
tag: LeetCode
---

Given an unsorted integer array, find the first missing positive integer.

#### For example
Given [1,2,0] return 3,

and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

<!--more-->

* 桶排序，应该nums[i]存储i+1,若nums[i] += i+1, 则交换nums[i], nums[nums[i]-1]

{% include_code LeetCode/Python/First-Missing-Positive.py %}
