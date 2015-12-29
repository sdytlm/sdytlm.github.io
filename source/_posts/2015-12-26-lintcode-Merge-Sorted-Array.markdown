---
layout: post
title: "Merge Sorted Array"
date: 2015-12-26
comments: true
categories: LintCode
tag: LintCode
---
### Merge Sorted Array
`Given two sorted integer arrays A and B, merge B into A as one sorted array.`

#### Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]

#### Note
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

<!--more-->

### Solution
* Time: O(N), Space: O(1)
* Tranverse A and B from the end
* index: index of the result
* i: index of A
* j: index of B
{% include_code LintCode/Merge-Sorted-Array.py %}
