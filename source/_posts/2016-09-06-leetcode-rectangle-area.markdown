---
layout: post
title: "Rectangle Area"
date: 2016-09-06
comments: true
categories: LeetCode
tag: LeetCode
---



Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

<!--more-->
### Solution
* 面积＝两个长方形面积－相交部分的面积
{% include_code LeetCode/Python/Rectangle-Area.py %}
