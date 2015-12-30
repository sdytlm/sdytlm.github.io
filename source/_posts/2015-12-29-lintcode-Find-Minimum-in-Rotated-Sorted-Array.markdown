---
layout: post
title: "Find Minimum in Rotated Sorted Array"
date: 2015-12-29
comments: true
categories: LintCode
tag: LintCode
---

### Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

#### Example
Given [4, 5, 6, 7, 0, 1, 2] return 0

#### Note
You may assume no duplicate exists in the array.

<!--more-->

### Solution
* 数组可以看成是两个ordered subarray 组成
* 前面那个subarray的任意值都比后面那个大
* 最小值一定在后面那个sub array中
* 如果num[front] > num[end]， 那么没有找到有序的sub array, 后移front
* 反之，则在sub array中，找最小值

{% include_code LintCode/Find-Minimum-in-Rotated-Array.py %}
