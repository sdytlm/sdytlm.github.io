---
layout: post
title: "Merge Sorted Array"
date: 2016-06-09
comments: true
categories: LeetCode
tag: LeetCode
---


Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#### Note
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

<!--more-->
### Solution
* From the end to front, Add the larger
{% include_code LeetCode/Python/Merge-Sorted-Array.py %}
