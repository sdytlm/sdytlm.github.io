---
layout: post
title: "Power of Two"
date: 2016-07-25
comments: true
categories: LeetCode
tag: LeetCode
---

Given an integer, write a function to determine if it is a powero two.

<!--more-->
### Solution
如果一个整数是2的幂，那么它的二进制形式最高位为1，其余各位为0

等价于：n & (n - 1) = 0，且n > 0

{% include_code LeetCode/Python/Power-of-Two.py %}
