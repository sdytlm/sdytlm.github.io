---
layout: post
title: "Increasing Triplet Subsequence"
date: 2016-07-02
comments: true
categories: LeetCode
tag: LeetCode
---

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 

such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Your algorithm should run in O(n) time complexity and O(1) space complexity.

#### Examples
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

<!--more-->
### Solution
```
初始令a = b = None

遍历数组nums，记当前元素为n

  若a为空或者a >= n，则令a = n；

  否则，若b为空或者b >= n，则令b = n；

  否则，返回true

遍历结束时，返回false。
```
{% include_code LeetCode/Python/Increasing-Triplet-Subsequence.py %}
