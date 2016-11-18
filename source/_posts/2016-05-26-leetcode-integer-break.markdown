---
layout: post
title: "Integer Break"
date: 2016-05-26
comments: true
categories: LeetCode
tag: LeetCode
---


Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

#### Example
 given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

#### Note 
you may assume that n is not less than 2.

#### Hint

There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

<!--more-->
### Solution
* Java
用所有的3作为因子，证明如下
[思路](https://discuss.leetcode.com/topic/45341/a-simple-explanation-of-the-math-part-and-a-o-n-solution)
{% include_code LeetCode/Java/Integer-Break.java %}

* Python
{% include_code LeetCode/Python/Integer-Break.py %}
