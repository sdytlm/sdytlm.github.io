---
layout: post
title: "Find Median from Data Stream"
date: 2016-08-12
comments: true
categories: LeetCode
tag: LeetCode
---


Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

#### Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

* void addNum(int num) - Add a integer number from the data stream to the data structure.
* double findMedian() - Return the median of all elements so far.

For example:
```
add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
```

<!--more-->

### Solution

* 维护两个最小堆small, large
* small中存数组比较小的部分的负数
* large存比较大的部分

{% include_code LeetCode/Python/Find-Median-from-Data-Stream.py %}
