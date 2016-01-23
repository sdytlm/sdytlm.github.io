---
layout: post
title: "Binary Representation"
date: 2016-01-18
comments: true
categories: LintCode
tag: LintCode
---

### Binary Representation

Given a (decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in as a string. If the fractional part of the number can not be represented accurately in binary with at most 32 characters, return ERROR.

#### Example
For n = "3.72", return "ERROR".

For n = "3.5", return "11.1".

<!--more-->
### Solution
* Convert Int part to HEX from right to left: integer = 5
    1. digit = integer % 2
    2. integer = integer / 2
* Convert Decimal part to HEX from left to right: e.g. decimal = 0.5 -> 0.1 (hex) 
    1. digit = int(decimal * 2)
    2. if decimal * 2 >= 1.0, then decimal = decimal * 2 - 1.0
    3. if decimal * 2 < 1.0, then decimal = decimal * 2
* If decimal part's hex is > 32bit, return ERROR

{% include_code LintCode/Binary-Representation.py %}
