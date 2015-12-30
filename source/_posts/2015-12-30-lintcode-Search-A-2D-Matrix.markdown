---
layout: post
title: "Search a 2D Matrix"
date: 2015-12-30
comments: true
categories: LintCode
tag: LintCode
---

### Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

#### Example
Consider the following matrix:
```
[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
```
Given target = 3, return true.

#### Challenge
O(log(n) + log(m)) time


<!--more-->

### Solution
* Time: O(logn + logm), Space: O(1)
`If A in (0,cols*rows), then matrix[A/cols][A%cols] could represent 2d matrix` 

{% include_code LintCode/Search-A-2D-Matrix.py%}
