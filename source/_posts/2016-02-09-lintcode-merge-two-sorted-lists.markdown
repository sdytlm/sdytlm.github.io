---
layout: post
title: "Merge Two Sorted Lists"
date: 2016-02-09
comments: true
categories: LintCode
tag: LintCode
---

### Merge Two Sorted Lists
Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

#### Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.

<!--more-->
### Solution
* Time: O(N)
* Use a dummy node as the head

{% include_code LintCode/Merge-Two-Sorted-Lists.py %}
