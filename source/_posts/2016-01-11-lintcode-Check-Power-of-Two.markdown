---
layout: post
title: "Check Power of Two"
date: 2016-01-11
comments: true
categories: LintCode
tag: LintCode
---
### Check Power of Two
Using O(1) time to check whether an integer n is a power of 2.

#### Example
For n=4, return true;

For n=5, return false;

#### Challenge
O(1) time
<!--more-->

### Solution
* Time: O(1)
> if x & (x-1) == 0, then x is the power of 2
{% include_code LintCode/Check-Power-of-Two.py %}
