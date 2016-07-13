---
layout: post
title: "Super Pow"
date: 2016-07-08
comments: true
categories: LeetCode
tag: LeetCode
---


Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

#### Example1:

a = 2
b = [3]

Result: 8

#### Example2:

a = 2
b = [1,0]

Result: 1024

<!--more-->
### Solution

* c mod m = (a ⋅ b) mod m  = [(a mod m) ⋅ (b mod m)] mod m
{% include_code LeetCode/Python/Super-Pow.py %}
