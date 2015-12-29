---
layout: post
title: "First Position of Target"
date: 2015-12-29
comments: true
categories: LintCode
tag: LintCode
---

### First Position of Target 

`For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.`

If the target number does not exist in the array, return -1.

#### Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

#### Challenge
If the count of numbers is bigger than 2^32, can your code work properly?


<!--more-->

### Solution
* Time: O(nlogn), Space: O(1)
* Binary Search
* Note: if you find one possible pos, you cannot guarantee it is the first
{% include_code LintCode/First-Position-of-Target.py %}
