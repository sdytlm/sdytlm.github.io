---
layout: post
title: "Jump Game"
date: 2016-01-26
comments: true
categories: LintCode
tag: LintCode
---


### Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

#### Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

#### Note
This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.
<!--more-->
### Solution
#### Greedy
* Time O(N)
    1.State:f[i]从i	出发能否到达最终位置
    2.Function:	f[j] = j + A[j] ≥ i,状态j转移到i,置为true	
    3.Initialization:第一个为true 的元素为	A.size()-1	
    4.Answer:递推到第0个元素时,若其值为	true 返回true	
{% include_code LintCode/Jump-Game-Greedy.py %}

#### DP
To be continued...
