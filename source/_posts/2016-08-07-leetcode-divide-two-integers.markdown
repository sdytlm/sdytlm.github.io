---
layout: post
title: "Divide Two Integers"
date: 2016-08-07
comments: true
categories: LeetCode
tag: LeetCode
---

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

<!--more-->
### Solution
因为不能用乘除和module,一般肯定想到是用位操作 除法也可以是减法，每次减去被除数，可以得到结果
优化 每次减去被除数左移k位的数, 结果加上相应`1<<k`

{% include_code LeetCode/Python/Divide-Two-Integers.py %}
