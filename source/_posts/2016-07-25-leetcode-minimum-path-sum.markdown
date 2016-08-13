---
layout: post
title: "Minimum Path Sum"
date: 2016-07-25
comments: true
categories: LeetCode
tag: LeetCode
---

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

#### Note: 
You can only move either down or right at any point in time.

<!--more-->
### Solution

* dp[i][j]: minimum path sum until grid[i][j]

{% include_code LeetCode/Python/Minimum-Path-Sum.py %}
