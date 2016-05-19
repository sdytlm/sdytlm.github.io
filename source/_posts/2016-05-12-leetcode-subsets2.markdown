---
layout: post
title: "Subsets II"
date: 2016-05-12
comments: true
categories: LeetCode
tag: LeetCode
---

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

#### Note
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.


#### Example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

<!--more-->
### Solution
* DFS + 剪枝
* 每次循环删掉已经加入到vector的元素

{% include_code LeetCode/Python/Subsets2.py %}
