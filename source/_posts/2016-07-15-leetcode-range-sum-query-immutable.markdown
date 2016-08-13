---
layout: post
title: "Range Sum Query - Immutable"
date: 2016-07-15
comments: true
categories: LeetCode
tag: LeetCode
---


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

#### Example:
Given nums = [-2, 0, 3, -5, 2, -1]

```
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

#### Note:
You may assume that the array does not change.

There are many calls to sumRange function.

<!--more-->
### Solution

* sums[i] = sums[i-1]+nums[i-1] (num[0]+num[1]...+num[i-1])
* sum of range [i,j] = sums[j+1]-sums[i]
{% include_code LeetCode/Python/Range-Sum-Query.py %}
