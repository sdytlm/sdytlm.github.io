---
layout: post
title: "Sort List"
date: 2016-02-09
comments: true
categories: LintCode
tag: LintCode
---


### Sort List

`Sort a linked list in O(n log n) time using constant space complexity.`

#### Example
Given 1-3->2->null, sort it to 1->2->3->null.

<!--more-->
### Solution
* Time: O(nlogn)
* Use merge sort and split the list into two sublist recursively and combine them.
{% include_code LintCode/Sort-List.py %}
