---
layout: post
title: "H-Index II"
date: 2016-05-10
comments: true
categories: LeetCode
tag: LeetCode
---

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

#### Hint
Expected runtime complexity is in O(log n) and the input is sorted.

<!--more-->
### Solution
* Binary Search: if `citations[mid] < len(citations)-mid, start=mid+1`

{% include_code LeetCode/Python/H-Index2.py %}

