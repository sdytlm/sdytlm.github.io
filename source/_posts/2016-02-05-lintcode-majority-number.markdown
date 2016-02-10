---
layout: post
title: "Majority Number"
date: 2016-02-05
comments: true
categories: LintCode
tag: LintCode
---

### Majority Number Show result 

`Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.`

#### Example
Given [1, 1, 1, 1, 2, 2, 2], return 1

#### Challenge
O(n) time and O(1) extra space


<!--more-->

### Solution
* The challenge require Moore's Voting Algorithm to solve
* Hash_map solution consume O(n), O(n)

{% include_code LintCode/Majority-Number.py %}
