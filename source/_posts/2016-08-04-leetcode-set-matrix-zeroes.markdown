---
layout: post
title: "Set Matrix Zeroes"
date: 2016-08-04
comments: true
categories: LeetCode
tag: LeetCode
---



Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

#### Follow up:
* Did you use extra space?
* A straight forward solution using O(mn) space is probably a bad idea.
* A simple improvement uses O(m + n) space, but still not the best solution.
* Could you devise a constant space solution?

<!--more-->
### Solution

* Reuse the first row and first column to store the flag for the following rows and folumns

{% include_code LeetCode/Python/Set-Matrix-Zeroes.py %}
