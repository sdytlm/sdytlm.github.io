---
layout: post
title: "Sqrt(x)"
date: 2015-12-30
comments: true
categories: LintCode
tag: LintCode
---

### Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

#### Example
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3

#### Challenge
O(log(x))


<!--more-->
### Solution
* Time: O(log N), Space: O(1)
* Binary search [0,x] find m (`m*m==x`)
{% include_code LintCode/SqrtX.py %}


