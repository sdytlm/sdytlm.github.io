---
layout: post
title: "Largest Number"
date: 2016-07-08
comments: true
categories: LeetCode
tag: LeetCode
---
Given a list of non negative integers, arrange them such that they form the largest number.

#### Example 
Given [3, 30, 34, 5, 9], 

The largest formed number is 9534330.

#### Note: 
The result may be very large, so you need to return a string instead of an integer.

<!--more-->
### Solution
* 对于两个备选数字a和b，如果str(a) + str(b) > str(b) + str(a)，则a在b之前，否则b在a之前

{% include_code LeetCode/Python/Largest-Number.py %}
