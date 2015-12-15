---
layout: post
title: "Compare Strings"
date: 2015-12-15
comments: true
categories: LintCode
tag: LintCode
---

### Compare Strings
#### Example
For A = "ABCD", B = "ACD", return true.

For A = "ABCD", B = "AABC", return false.

#### Note
The characters of B in A are not necessary continuous or ordered.

<!-- more -->

### Solution

* Array `characters[256]` record all possible letters. Initialize it as all zeros
* Scan the array A and characters[A[i]-'A']++
* Scan the array B, characters[B[i]-'A']--. If find any characters[B[i]-'A'] <= 0. Then Array A cannot have this character of Array B.

{% include_code LintCode/Compare-Strings.py %}
