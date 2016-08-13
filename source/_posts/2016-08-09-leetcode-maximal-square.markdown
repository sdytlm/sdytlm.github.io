---
layout: post
title: "Maximal Square"
date: 2016-08-09
comments: true
categories: LeetCode
tag: LeetCode
---


Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#### Example
Given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
Return 4.

<!--more-->
### Solution
`dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1`
上式中，dp[x][y]表示以坐标(x, y)为右下角元素的全1正方形矩阵的最大长度（宽度）

{% include_code LeetCode/Python/Maximal-Square.py %}
