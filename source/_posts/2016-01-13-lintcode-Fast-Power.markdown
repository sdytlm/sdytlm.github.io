---
layout: post
title: "Fast Power"
date: 2016-01-13
comments: true
categories: LintCode
tag: LintCode
---

### Fast Power


Calculate the a^n % b where a, b and n are all 32 bit integers.

#### Example
For 231 % 3 = 2

For 100^1000 % 1000 = 0

#### Challenge
O(logn)

<!--more-->

### Solution
* Time: O(logn)

> (a * b) % p = ((a % p) * (b % p)) % p 

* a^2 %b = ((a%b) * (a%b))%b
* a^3 %b = ((a^2%b) * (a%b))%b
{% include_code LintCode/Fast-Power.py %}
