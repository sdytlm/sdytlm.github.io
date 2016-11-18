---
layout: post
title: "K Smallest Element in a Sorted Matrix"
date: 2016-09-07
comments: true
categories: LeetCode
tag: LeetCode
---

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

#### Example:
```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```
#### Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

<!--more-->
### Solution
* 二分查找，start = matrix[0][0], end = matrix[-1][-1]
* mid = (start+end)/2，统计小于等于mid的个数（统计时，以左下角为起点)

{% include_code LeetCode/Python/Kth-Smallest-Element-in-A-Sorted-Matrix.py %}

