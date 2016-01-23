---
layout: post
title: "Trailing Zeros"
date: 2016-01-18
comments: true
categories: LintCode
tag: LintCode
---


### Trailing Zeros

> Write an algorithm which computes the number of trailing zeros in n factorial.

#### Example
11! = 39916800, so the out should be 2

#### hallenge
O(log N) time

<!--more-->
### Solution
* The idea is to consider prime factors of a factorial n. A trailing zero is always produced by prime factors 2 and 5. If we can count the number of 5s and 2s, our task is done. Consider the following examples.

* n = 5: There is one 5 and 3 2s in prime factors of 5! (2 * 2 * 2 * 3 * 5). So count of trailing 0s is 1.

* n = 11: There are two 5s and eight 2s in prime factors of 11! (2 8 * 34 * 52 * 7). So count of trailing 0s is 2.

* the number of 2s in prime factors is always more than or equal to the number of 5s. So if we count 5s in prime factors, we are done. 

* How to count total number of 5s in prime factors of n!? A simple way is to calculate floor(n/5). 

* Time: O(logn)
{% include_code LintCode/Trailing-Zeros.py %}

