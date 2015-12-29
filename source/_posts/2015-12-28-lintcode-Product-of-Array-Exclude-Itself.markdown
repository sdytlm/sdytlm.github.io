---
layout: post
title: "Product of Array Exclude Itself"
date: 2015-12-28
comments: true
categories: LintCode
tag: LintCode
---

### Product of Array Exclude Itself

Given an integers array A.

`Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.`

#### Example
For A = [1, 2, 3], return [6, 3, 2].

<!--more-->

### Solution
* Time: O(N^2), Space: O(N)
{% include_code LintCode/Product-Of-Array-Exclude-Itself.py %}

