---
layout: post
title: "Remove Duplicates from Sorted Array"
date: 2015-12-22
comments: true
categories: LintCode
tag: LintCode
---


### Remove Duplicates from Sorted Array

`Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.`

#### Note
Do not allocate extra space for another array, you must do this in place with constant memory.


#### Example
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

<!--more-->

### Solution
* Two pointer **start** and **i**: one record next unduplicated position, the is used to tranverse the whole array


{% include_code LintCode/Remove-Duplicates-from-Sorted-Array.py %}
