---
layout: post
title: "Range Sum Query- Mutable"
date: 2016-08-14
comments: true
categories: LeetCode
tag: LeetCode
---


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
#### Example:
```
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```
#### Note:
* The array is only modifiable by the update function.
* You may assume the number of calls to update and sumRange function is distributed evenly.

<!--more-->
### Solution
[线段树Fenwick Tree](https://www.hrwhisper.me/binary-indexed-tree-fenwick-tree/)

{% include_code LeetCode/Python/Range-Sum-Query-Mutable.py %}
