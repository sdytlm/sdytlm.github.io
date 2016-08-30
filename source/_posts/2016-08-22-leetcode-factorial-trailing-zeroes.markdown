---
layout: post
title: "Factorial Trailing Zeroes"
date: 2016-08-22
comments: true
categories: LeetCode
tag: LeetCode
---


Given an integer n, return the number of trailing zeroes in n!.

#### Note: 
Your solution should be in logarithmic time complexity.

<!--more-->
### Solution
`n!后缀0的个数 = n!质因子中5的个数
              = floor(n/5) + floor(n/25) + floor(n/125) + ....`

{% include_code LeetCode/Python/Factorial-Trailing-Zeroes.py %}
