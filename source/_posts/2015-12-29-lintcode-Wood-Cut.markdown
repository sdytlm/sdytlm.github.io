---
layout: post
title: "Wood Cut"
date: 2015-12-29
comments: true
categories: LintCode
tag: LintCode
---

### Wood Cut

`Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.`

#### Example
For L=[232, 124, 456], k=7, return 114.

#### Note
You couldn't cut wood into float length.

#### Challenge
O(n log Len), where Len is the longest length of the wood.


<!--more-->

### Solution
* Time: O(N log len), Space: O(N)
* Binary search, The idea is [here](http://algorithm.yuanbin.me/zh-cn/binary_search/wood_cut.html)

{% include_code LintCode/Wood-Cut.py %}
