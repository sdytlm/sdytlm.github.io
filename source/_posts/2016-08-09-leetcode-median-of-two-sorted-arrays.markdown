---
layout: post
title: "Median of Two Sorted Arrays"
date: 2016-08-09
comments: true
categories: LeetCode
tag: LeetCode
---

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

#### Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

#### Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

<!--more-->
### Solution
* 这个问题实际上是查找底(m+n)/2和第(m+n)/2+1个元素. (第k个元素)
* 二分查找，把k分成2部分pa=`min(k/2, len(a))`和pb=k-pa
* 比较A[pa]于B[pb]

** if (`A[pa]<B[pb]`), which means the elements from A[0] to A[pa] must exist in the first Kth elements.二分查找下一个的时候就不需要考虑A[0:pa]，他们一定在前k个元素里

** if (`A[pa]>B[pb]`), the same procedure is applied but we "cut" the B array.
{% include_code LeetCode/Python/Median-of-Two-Sorted-Arrays.py %}
