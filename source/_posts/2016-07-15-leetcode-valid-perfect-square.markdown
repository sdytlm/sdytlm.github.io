---
layout: post
title: "Valid Perfect Square"
date: 2016-07-15
comments: true
categories: LeetCode
tag: LeetCode
---



Given a positive integer num, write a function which returns True if num is a perfect square else False.

#### Note: 
Do not use any built-in library function such as sqrt.

#### Example 1:

Input: 16

Returns: True

#### Example 2:

Input: 14

Returns: False

<!--more-->
### Solution

* Binary Search (2,num/2+1)

{% include_code LeetCode/Python/Valid-Perfect-Square.py %}
