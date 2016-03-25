---
layout: post
title: "Permutations II"
date: 2016-03-16
comments: true
categories: LintCode
tag: LintCode 
---


Given a list of numbers with duplicate number in it. Find all unique permutations.

#### Example
For numbers [1,2,2] the unique permutations are:
```
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
```

<!--more-->
### Solution
* DFS
{% include_code LintCode/Permutations2.py %}
