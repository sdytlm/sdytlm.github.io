---
layout: post
title: "Merge K Sorted Lists"
date: 2016-08-22
comments: true
categories: LeetCode
tag: LeetCode
---


Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

<!--more-->
### Solution
* 维护一个最小堆，保存当前各个List中的第一个节点
* 最小堆的第一个节点就是当前最小节点

{% include_code LeetCode/Python/Merge-k-sorted-lists.py %}
