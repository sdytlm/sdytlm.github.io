---
layout: post
title: "Power of Three"
date: 2016-07-05
comments: true
categories: LeetCode
tag: LeetCode
---

Given an integer, write a function to determine if it is a power of three.

#### Follow up:
Could you do it without using any loop / recursion?

<!--more-->
### Solution
* Java:Find the maximum integer(1162261467) that is a power of 3 and check if it is a multiple of the given input. 
{% include_code LeetCode/Java/Power-of-Three.java %}

* Python: 求对数，然后乘方，判断得数是否相等

{% include_code LeetCode/Python/Power-of-Three.py %}
