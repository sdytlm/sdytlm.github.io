---
layout: post
title: "Flip Bits"
date: 2015-12-31
comments: true
categories: LintCode
tag: LintCode
---

### Flip Bits

Determine the number of bits required to flip if you want to convert integer n to integer m.

#### Example
Given n = 31 (11111), m = 14 (01110), return 2.

#### Note
Both n and m are 32-bit integers.

<!--more-->

### Solution
> if a<0, a's binary = 2^32 - abs(a)

{% include_code LintCode/Flip-Bits.py %}

