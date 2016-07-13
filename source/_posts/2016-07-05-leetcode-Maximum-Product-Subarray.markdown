---
layout: post
title: "Maximum Product Subarray"
date: 2016-07-05
comments: true
categories: LeetCode
tag: LeetCode
---



Find the contiguous subarray within an array (containing at least one number) which has the largest product.

#### Example
Given the array [2,3,-2,4],
The contiguous subarray [2,3] has the largest product = 6.

<!--more-->
### Solution
* 用数组pos[i]维护原始数组前i个数的子数组乘积中正数的最大值
* 用数组neg[i]维护原始数组前i个数的子数组乘积中负数的最小值

{% include_code LeetCode/Python/Maximum-Product-Subarray.py %}
