---
layout: post
title: "Permutations II"
date: 2016-08-25
comments: true
categories: leetcode
tag: leetcode
---



Given a collection of numbers that might contain duplicates, return all possible unique permutations.

#### Example
[1,1,2] have the following unique permutations:
```
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```
<!--more-->
### Solution
* 递归，注意去掉nums[i]==nums[i-1]的情况

{% include_code LeetCode/Python/Permutations2.py %}
