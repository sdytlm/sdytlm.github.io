---
layout: post
title: "Unique Paths"
date: 2016-01-12
comments: true
categories: LintCode
tag: LintCode
---

### Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

<!--more-->

### Solution
* Time: O(n^2)
* path[m][n]: number of unique paths for m * n grid
> paths[m][n] = paths[m-1][n] + paths[m][n-1]

{% include_code LintCode/Unique-Paths.py %}
