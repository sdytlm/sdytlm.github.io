---
layout: post
title: "Pascal's Triangle II"
date: 2016-07-31
comments: true
categories: LeetCode
tag: LeetCode
---

Given an index k, return the kth row of the Pascal's triangle.

#### Example
given k = 3,
Return [1,3,3,1].

#### Note:
Could you optimize your algorithm to use only O(k) extra space?

<!--more-->
### Solution

* 每次循环开始前在dp前面插入１，ret[i] = ret[i]+ret[i+1],
{% include_code LeetCode/Java/Pascal-Triangle2.java %}


* Python
{% include_code LeetCode/Python/Pascal-Triangle2.py %}
