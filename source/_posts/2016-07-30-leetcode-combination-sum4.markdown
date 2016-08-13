---
layout: post
title: "Combination Sum4"
date: 2016-07-30
comments: true
categories: LeetCode
tag: LeetCode
---

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

#### Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
```
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
```
#### Note:
Different sequences are counted as different combinations.

Therefore the output is 7.
#### Follow up:
* What if negative numbers are allowed in the given array?
* How does it change the problem?
* What limitation we need to add to the question to allow negative numbers?


<!--more-->
### Solution
状态转移方程：dp[x + y] += dp[x]

其中dp[x]表示生成数字x的所有可能的组合方式的个数。

{% include_code LeetCode/Python/Combination-Sum4.py %}
