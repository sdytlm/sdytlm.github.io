---
layout: post
title: "Fraction to Recurring Decimal"
date: 2016-06-16
comments: true
categories: LeetCode
tag: LeetCode
---

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

#### Example

* Given numerator = 1, denominator = 2, return "0.5".
* Given numerator = 2, denominator = 1, return "2".
* Given numerator = 2, denominator = 3, return "0.(6)".

#### Hint

* No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
* Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
* Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

<!--more-->
### Solution

{% include_code LeetCode/Python/Fraction-to-Recurring-Decimal.py %}
