---
layout: post
title: "Multiply-Strings"
date: 2016-07-14
comments: true
categories: LeetCode
tag: LeetCode
---


Given two numbers represented as strings, return multiplication of the numbers as a string.

#### Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.

<!--more-->
### Solution

算法的关键是要先将两个字符串翻转过来，然后按位进行相乘，相乘后的数不要着急进位，而是存储在一个数组里面，然后将数组中的数对10进行求余（%），就是这一位的数，然后除以10，即/10，就是进位的数。注意最后要将相乘后的字符串前面的0去掉。

{% include_code LeetCode/Python/Multiply-Strings.py %}
