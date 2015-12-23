---
layout: post
title: "Subarry Sum"
date: 2015-12-22
comments: true
categories: LintCode
tag: LintCode
---

### Subarray Sum

`Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.`

#### Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

#### Note
There is at least one subarray that it's sum equals to zero.

<!--more-->
### Solution

* Bruce Force: O(N^2)
{% include_code LintCode/Subarray-Sum.py %}

* Hash table: O(N)
    * Hash Table: {[sum: index+1]}
    * You calculate the sum of substrings and maintain the hash table, if you find the sum appear again, you find the substring
    * For example: [hash-table[sum],x,x,x,i] then[x,x,x,i] is the string
    * Consider when `sum==0`, we have to initialize the hash-table with {[0:0]}
{% include_code LintCode/Subarray-Sum-hashtable.py %}

