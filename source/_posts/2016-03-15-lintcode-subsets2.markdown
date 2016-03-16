---
layout: post
title: "Subsets II"
date: 2016-03-15
comments: true
categories: LintCode
tag: LintCode 
---

Given a list of numbers that may has duplicate numbers, return all possible subsets

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

#### Example
If S = [1,2,2], a solution is:
```
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

<!--more-->

#### Solution
* Use DFS to solve the problem.
* enumerate is useful.

{% include_code LintCode/Subsets2.py %}
