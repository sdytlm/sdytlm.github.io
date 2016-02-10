---
layout: post
title: "Remove Nth Node from End of List"
date: 2016-02-08
comments: true
categories: LintCode
tag: LintCode
---

### Remove Nth Node from End of List

`Given a linked list, remove the nth node from the end of list and return its head.`

#### Example
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.

#### Note
The minimum number of nodes in list is n.

#### Challenge
O(n) time

<!--more-->
### Solution
* Time O(n)
* Find the length of list and count which to delete
{% include_code LintCode/Remove-Nth-Node-From-End-Of-List.py %}
