---
layout: post
title: "Surrounded Region"
date: 2016-05-26
comments: true
categories: LeetCode
tag: LeetCode
---

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

#### Example
```
X X X X
X O O X
X X O X
X O X X
```
After running your function, the board should be:

```
X X X X
X X X X
X X X X
X O X X
```

<!--more-->
###Solution

* From left,right,top and bottom, mark all path of 'O' to 'D'. Replace the left 'O' with 'X'

{% include_code LeetCode/Python/Surrounded-Regions.py %}
