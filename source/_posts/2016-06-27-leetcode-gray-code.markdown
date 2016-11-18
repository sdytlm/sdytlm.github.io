---
layout: post
title: "Gray Code"
date: 2016-06-27
comments: true
categories: LeetCode
tag: LeetCode
---

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

#### Example
Given n = 2, return [0,1,3,2]. Its gray code sequence is:

```
00 - 0
01 - 1
11 - 3
10 - 2
```

#### Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

<!--more-->
### Solution
* 一部分是n-1位格雷码，再加上 1<<(n-1)和n-1位格雷码的逆序的和。
* Java
{% include_code LeetCode/Java/Gray-Code.java %}


* Python
{% include_code LeetCode/Python/Gray-Code.py %}
