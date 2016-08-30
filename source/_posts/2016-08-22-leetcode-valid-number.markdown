---
layout: post
title: "Valid Number"
date: 2016-08-22
comments: true
categories: LeetCode
tag: LeetCode
---

Validate if a given string is numeric.

Some examples:
```
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
```
#### Note: 
It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

<!--more-->
* 小数点前和后没有数字都是合法的
* 科学计数法后面也可以是负数
### Solution

{% include_code LeetCode/Python/Valid-Number.py %}
