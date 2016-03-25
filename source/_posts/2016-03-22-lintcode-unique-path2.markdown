---
layout: post
title: "Unique Path II"
date: 2016-03-22
comments: true
categories: LintCode
tag: LintCode 
---

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

#### Example
There is one obstacle in the middle of a 3x3 grid as illustrated below.
```
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
```
The total number of unique paths is 2.

<!--more-->
### Solution
* DP
* Be carefur the case, dp[1][1], dp[i][1],dp[1][j] and dp[i][j]
{% include_code LintCode/Unique-Path2.py %}
