---
layout: post
title: "Longest Consecutive Sequence"
date: 2016-08-06
comments: true
categories: LeetCode
tag: LeetCode
---

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#### Example:
Given [100, 4, 200, 1, 3, 2],

The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

<!--more-->

### Solution
* hash_map:{nums[i]:False}
* 使用一个哈希表，在Python中是字典dict数据类型。dict中的映射关系是{x in num：False}，这个表示num中的x元素没有被访问过，如果被访问过，则为True。如果x没有被访问过，检查x+1，x+2...，x-1，x-2是否在dict中，如果在dict中，就可以计数。最后可以求得最大长度。

{% include_code LeetCode/Python/Longest-Consecutive-Sequence.py %}
