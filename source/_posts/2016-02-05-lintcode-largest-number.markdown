---
layout: post
title: "Largest Number"
date: 2016-02-05
comments: true
categories: LintCode
tag: LintCode
---

### Largest Number

`Given a list of non negative integers, arrange them such that they form the largest number.`

#### Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.

#### Note
The result may be very large, so you need to return a string instead of an integer.

#### Challenge
Do it in O(nlogn) time complexity.

<!--more-->

### Solution
* Time: O(nlogn)
* Write a customized comparator for the list:
* The comparator is used to compare if `yx > xy`
* Use this comparator to sort the list, then connect all elements in the list.
{%include_code LintCode/Largest-Number.py %}
