---
layout: post
title: "Find Peak Element"
date: 2015-12-30
comments: true
categories: LintCode
tag: LintCode
---

### Find Peak Element 

There is an integer array which has the following features:

* The numbers in adjacent positions are different.
* A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peek if:

`A[P] > A[P-1] && A[P] > A[P+1]`

Find a peak element in this array. Return the index of the peak.

#### Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)

#### Note
The array may contains multiple peeks, find any of them.

#### Challenge
Time complexity O(logN)

<!--more-->
### Solution
* Time: O(log n)
* 若A[mid] > A[mid - 1] && A[mid] < A[mid + 1]，则找到一个peak为A[mid]；
* 若A[mid - 1] > A[mid]，则A[mid]左侧必定存在一个peak，可用反证法证明：若左侧不存在peak，则A[mid]左侧元素必满足A[0] > A[1] > ... > A[mid -1] > A[mid]，与已知A[0] < A[1]矛盾，证毕。
* 同理可得若A[mid + 1] > A[mid]，则A[mid]右侧必定存在一个peak

{% include_code LintCode/Find-Peak-Element.py %}
