---
layout: post
title: "Search a 2D Matrix II"
date: 2016-08-07
comments: true
categories: LeetCode
tag: LeetCode
---


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.

#### Example

Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
Given target = 5, return true.

Given target = 20, return false.

<!--more-->
### Solution
* Java: Best Solution O(M+N)
{% include_code LeetCode/Java/Search-a-2D-Matrix2.java %}

* 搜索合适的行，二分查找该行
{% include_code LeetCode/Python/Search-2D-Matrix2.py %}
