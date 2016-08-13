---
layout: post
title: "Max Sum of Rectangle No Larger Than K"
date: 2016-08-09
comments: true
categories: LeetCode
tag: LeetCode
---



Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

#### Example:
```
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
```
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

#### Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

<!--more-->
### Solution

* [Kadane's Algorithm](https://discuss.leetcode.com/topic/48875/accepted-c-codes-with-explanation-and-references)

{% include_code LeetCode/Python/Max-Sum-of-Rectangle-No-Larger-Than-K.py %}
