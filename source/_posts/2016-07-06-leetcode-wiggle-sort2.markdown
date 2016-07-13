---
layout: post
title: "Wiggle Sort II"
date: 2016-07-06
comments: true
categories: LeetCode
tag: LeetCode
---


Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

#### Example:
1. Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
2. Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

#### Note:
You may assume all input has valid answer.

#### Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

<!--more-->
### Solution
#### O(nlog(n)) + O(n)
1. 对原数组排序，得到排序后的辅助数组snums

2. 对原数组的偶数位下标填充snums的末尾元素 (current biggest)

3. 对原数组的奇数位下标填充snums的末尾元素

{% include_code LeetCode/Python/Wiggle-Sort2.py %}

#### O(n) + O(1)
[Ideas](https://discuss.leetcode.com/topic/32929/o-n-o-1-after-median-virtual-indexing/2)
