---
layout: post
title: "Next Permutation"
date: 2016-01-25
comments: true
categories: LintCode
tag: LintCode
---


### Next Permutation

Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

#### Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]

#### Note
The list may contains duplicate integers.

<!--more-->
### Solution
* Time: O(N)
* From right to left, find the first digit (num[front]) which violate the increase trend
* From right to left, find the first digit (num[end] > num[front])
* Swap the end and front
* Reverse all digits on the right side of num[front]
{% include_code LintCode/Next-Permutation.py  %}
