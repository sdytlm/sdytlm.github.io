---
layout: post
title: "Number of Islands"
date: 2016-07-21
comments: true
categories: LeetCode
tag: LeetCode
---

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#### Example 1:

```
11110
11010
11000
00000
```
Answer: 1

#### Example 2:

```
11000
11000
00100
00011
```
Answer: 3

<!--more-->
### Solution
* Flood Fill Algorithm
{% include_code LeetCode/Python/Number-of-Islands.py %}
