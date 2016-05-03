---
layout: post
title: "Backpack"
date: 2016-03-25
comments: true
categories: LintCode
tag: LintCode 
---


Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

#### Note
You can not divide any item into small pieces.

#### Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

#### Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

<!--more-->

### Solution

{% include_code LintCode/Backpack.py %}



