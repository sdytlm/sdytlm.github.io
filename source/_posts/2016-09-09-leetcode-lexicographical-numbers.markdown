---
layout: post
title: "Lexicographical Numbers"
date: 2016-09-09
comments: true
categories: LeetCode
tag: LeetCode
---



Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

<!--more-->
### Solution
递归的思路如下:
```
def solve(m):
    result.append(m)
    if m * 10 <= n: solve(m * 10)
    if m < n and m % 10 < 9: solve(m + 1)
```
{% include_code LeetCode/Python/Lexicographical-Numbers.py %}
