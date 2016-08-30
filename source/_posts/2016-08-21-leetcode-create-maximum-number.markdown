---
layout: post
title: "Create Maximum Number"
date: 2016-08-21
comments: true
categories: LeetCode
tag: LeetCode
---

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

#### Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

#### Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

#### Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

<!--more-->
### Solution

1. 从数组nums中挑选出t个数，在保持元素相对顺序不变的情况下，使得选出的子数组最大化。

2. 在保持元素相对顺序不变的前提下，将数组nums1与数组nums2合并，使合并后的数组最大化。

{% include_code LeetCode/Python/Create-Maximum-Number.py %}
