---
layout: post
title: "Update Bits"
date: 2016-01-08
comments: true
categories: LintCode
tag: LintCode
---

### Update Bits

Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e g , M becomes a substring of N located at i and starting at j)

#### Example
Given N=(10000000000)2, M=(10101)2, i=2, j=6

return N=(10001010100)2

#### Note
In the function, the numbers N and M will given in decimal, you should also return a decimal number.

#### Challenge
Minimum number of operations?

#### Clarification
You can assume that the bits j through i have enough space to fit all of M. That is, if M=10011， you can assume that there are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.

<!--more -->

### Solution
* Time O(1)

Buid a Mask: `11111100000011111` in [i,j], the bits are all 0

{% include_code LintCode/Update-Bits.py %}
