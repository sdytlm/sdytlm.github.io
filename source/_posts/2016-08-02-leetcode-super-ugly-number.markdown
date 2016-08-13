---
layout: post
title: "Super Ugly Number"
date: 2016-08-02
comments: true
categories: LeetCode
tag: LeetCode
---

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

#### Note:
1. 1 is a super ugly number for any given primes.
2. The given numbers in primes are in ascending order.
3. 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.

<!--more-->

### Solution
* priority queue
使用Python生成器和heapq.merge，将primes中各个元素的质数倍数合并在一起

{% include_code LeetCode/Python/Super-Ugly-Number.py %}
