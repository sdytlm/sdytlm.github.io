---
layout: post
title: "Interleaving String"
date: 2016-03-24
comments: true
categories: LintCode
tag: LintCode 
---


Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

#### Example
For s1 = "aabcc", s2 = "dbbca"

When s3 = "aadbbcbcac", return true.

When s3 = "aadbbbaccc", return false.

#### Challenge
O(n2) time or better

<!--more-->

### Solution
* dp[i][j]: if s1[i] and s2[j] could constitue s3[i+j+1]
{% include_code LintCode/Interleaving-String.py %}

