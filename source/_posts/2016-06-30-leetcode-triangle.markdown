---
layout: post
title: "Triangle"
date: 2016-06-30
comments: true
categories: LeetCode
tag: LeetCode
---

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

#### Example
Given the following triangle
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

#### Note
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

<!--more-->
### Solution
* dp[j]: 表示某一行每一列的最小值
* 从下往上便利
* dp[j] = triangle[i][j]+min(dp[j],dp[j+1]) 

* Java
{% include_code LeetCode/Java/Triangle.java %}
* Python
{% include_code LeetCode/Python/Triangle.py %}
