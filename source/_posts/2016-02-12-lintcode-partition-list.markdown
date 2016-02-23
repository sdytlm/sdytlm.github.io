---
layout: post
title: "Partition List"
date: 2016-02-12
comments: true
categories: LintCode
tag: LintCode
---

### Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

#### For example,
Given 1->4->3->2->5->2->null and x = 3,

return 1->2->2->4->3->5->null.

<!--more-->
### Solution
* Time: O(N)
* Two new list to contain node smaller than x and larger than x
* Connect two list

{% include_code LintCode/Partition-List.py %}
