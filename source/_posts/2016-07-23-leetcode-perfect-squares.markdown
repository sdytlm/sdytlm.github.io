---
layout: post
title: "Perfect Squares"
date: 2016-07-23
comments: true
categories: LeetCode
tag: LeetCode
---


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

<!--more-->
### Solution
* 初始化将dp数组置为无穷大；令dp[y * y] = 1，其中：y * y <= n

* 状态转移方程：

`dp[x + y * y] = min(dp[x + y * y], dp[x] + 1)`

* 其中：dp [i] 表示凑成i所需的平方和数字的最小个数，并且 x + y * y <= n

{% include_code LeetCode/Python/Perfect-Squares.py %}
