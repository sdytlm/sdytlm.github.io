---
layout: post
title: "Roman to Integer"
date: 2016-07-04
comments: true
categories: LeetCode
tag: LeetCode
---

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

<!--more-->
### Solution
* Java: `s[i] <s[i+1]`
{% include_code LeetCode/Java/Roman-to-Integer.java %}

* Python: 要区分几个特殊情况，CM, IV, IX
{% include_code LeetCode/Python/Roman-to-Integer.py %}

