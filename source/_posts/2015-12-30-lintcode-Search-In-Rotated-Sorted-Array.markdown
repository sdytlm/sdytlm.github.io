---
layout: post
title: "Search in Rotated Sorted Array"
date: 2015-12-30
comments: true
categories: LintCode
tag: LintCode
---

### Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

#### Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

<!--more-->
### Solution
* Time: O(log n)
* 若target == A[mid]，索引找到，直接返回
* 寻找局部有序数组，分析A[mid]和两段有序的数组特点，由于旋转后前面有序数组最小值都比后面有序数组最大值大。故若A[start] < A[mid]成立，则start与mid间的元素必有序（要么是前一段有序数组，要么是后一段有序数组，还有可能是未旋转数组）。
* 接着在有序数组A[start]~A[mid]间进行二分搜索，但能在A[start]~A[mid]间搜索的前提是A[start] <= target <= A[mid]。
* 接着在有序数组A[mid]~A[end]间进行二分搜索，注意前提条件。
{% include_code LintCode/Search-In-Rotated-Sorted-Array.py %}
