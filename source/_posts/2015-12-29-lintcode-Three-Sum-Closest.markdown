---
layout: post
title: "Three Sum Closest"
date: 2015-12-29
comments: true
categories: LintCode
tag: LintCode
---

### 3Sum Closest

`Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.`

#### Example
For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

#### Note
You may assume that each input would have exactly one solution.

#### Challenge
O(n^2) time, O(1) extra space

<!--more-->

### Solution
* Time: O(N^2), Space O(1)
* Idea is similar to [Three Sum ](http://sdytlm.github.io/blog/2015/12/28/lintcode-Three-Sum/)

{% include_code LintCode/Three-Sum-Closet.py %}
