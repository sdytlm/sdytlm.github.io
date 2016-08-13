---
layout: post
title: "Bitwise And of Numbers Range"
date: 2016-07-18
comments: true
categories: LeetCode
tag: LeetCode
---

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

<!--more-->
### Solution

最后的与肯定是从某一位开始都相同，那么我们只需要看最大和最小的两个数，从哪一位开始是相同的，也就是看最大和最小的两个值的高几位相同。 当然我们也可以使用从高位往地位判断，有多少位是相同的。

{% include_code LeetCode/Python/Bitwise-and-of-Numbers-Range.py %}
