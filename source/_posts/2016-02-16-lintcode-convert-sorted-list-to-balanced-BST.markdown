---
layout: post
title: "Convert Sorted List to Balanced BST"
date: 2016-02-16
comments: true
categories: LintCode
tag: LintCode
---



### Convert Sorted List to Balanced BST

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

#### Example
```
                   2
1->2->3  =>   / \
                 1   3

```
<!--more-->
### Solution
* Time: O(n^2)
* We dont have to find the middle node in each interation.
* if you change the input parameters and add `left`,`right` and write another helper func to help iteration, could get O(N)

{% include_code LintCode/Convert-Sorted-List-to-BST.py %}
