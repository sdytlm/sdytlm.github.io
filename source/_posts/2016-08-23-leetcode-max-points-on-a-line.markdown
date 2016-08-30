---
layout: post
title: "Max Points on a Line"
date: 2016-08-23
comments: true
categories: LeetCode
tag: LeetCode
---



Given n points on a 2D plane, find the maximum number of points that lie on the same straight line

<!--more-->
### Solution
* O(n^2*log(n))
枚举起点i，与终点j，依次计算i，j的斜率，统计斜率相同的点的个数的最大值

{% include_code LeetCode/Python/Max-Points-on-a-line.py %}
