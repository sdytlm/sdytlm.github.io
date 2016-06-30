---
layout: post
title: "Missing Number"
date: 2016-06-16
comments: true
categories: LeetCode
tag: LeetCode
---

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

#### Example
n nums = [0, 1, 3] return 2.

#### Note
Yourlgorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

<!--more-->
### Solution
* X ^ 0 ^ X = 0
* X ^ 0 = X
{% include_code LeetCode/Python/Missing-Number.py %}
