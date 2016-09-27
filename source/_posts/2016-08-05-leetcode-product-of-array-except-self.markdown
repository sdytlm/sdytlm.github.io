---
layout: post
title: "Product of Array Except Self"
date: 2016-08-05
comments: true
categories: LeetCode
tag: LeetCode
---


Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

#### For example: 
given [1,2,3,4], return [24,12,8,6].

#### Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

<!--more-->
### Solution
* 先o(n)　时间累乘nums[i]左边
* 再O(n) 累乘nums[i]右边

{% include_code LeetCode/Java/Product-of-Array-Except-Self.java %}
