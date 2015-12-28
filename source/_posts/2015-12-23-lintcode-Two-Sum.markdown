---
layout: post
title: "Two Sum"
date: 2015-12-23
comments: true
categories: LintCode
tag: LintCode
---

### Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

#### Example
numbers=[2, 7, 11, 15], target=9

return [1, 2]

#### Note
You may assume that each input would have exactly one solution

#### Challenge
Either of the following solutions are acceptable:

* O(n) Space, O(nlogn) Time
* O(n) Space, O(n) Time

<!--more-->

### Solution
* Space: O(N), Time: O(nlogn)
{% include_code LintCode/Two-Sum.py %}

* Space: O(N), Time: O(N)
先排序，两个指针，分别从头尾开始，向中间靠拢，直到发现目标
{% include_code LintCode/Two-Sum2.py %}
