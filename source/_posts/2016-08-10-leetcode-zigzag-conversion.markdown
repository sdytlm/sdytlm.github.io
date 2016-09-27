---
layout: post
title: "ZigZag Conversion"
date: 2016-08-10
comments: true
categories: LeetCode
tag: LeetCode
---

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string text, int nRows);
```
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

<!--more-->
### Solution
* 模拟从第一行插入到numRows-1行，再倒回去，依次往复

* Java:
{% include_code LeetCode/Java/Zigzag-Conversion.java %}

* Python
{% include_code LeetCode/Python/Zigzag-Conversion.py %}
