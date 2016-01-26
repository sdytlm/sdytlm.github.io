---
layout: post
title: "Single Number"
date: 2016-01-22
comments: true
categories: LintCode
tag: LintCode
---

### Single Number

> Given 2 * n + 1 numbers, every numbers occurs twice except one, find it.

#### Example
Given [1,2,2,1,3,4,3], return 4

#### Challenge
One-pass, constant extra space.

<!--more-->
### Solution
* Time O(N), Space O(1)
* `x ^ x=0 和	x ^ 0=x` 可将给定数组的所有数依次异或,最后保留的即为结果。
{% include_code LintCode/Single-Number.py %}
