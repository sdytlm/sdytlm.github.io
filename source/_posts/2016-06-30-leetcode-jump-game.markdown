---
layout: post
title: "Jump Game"
date: 2016-06-30
comments: true
categories: LeetCode
tag: LeetCode
---


Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

### Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

<!--more-->
### Solution
* index_true: current reachable index
* if nums[i] + i > index_true, then index_true = i

{% include_code LeetCode/Python/Jump-Game.py %}
