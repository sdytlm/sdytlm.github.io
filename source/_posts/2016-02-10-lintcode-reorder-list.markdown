---
layout: post
title: "Reorder List"
date: 2016-02-10
comments: true
categories: LintCode
tag: LintCode
---

### Reorder List

Given a singly linked list L: L0→L1→…→L(n-1)→Ln,

reorder it to: L0→Ln→L1→Ln-1→L2→L(n-2)→…

You must do this in-place without altering the nodes' values.

#### Example

Given 1->2->3->4->null, reorder it to 1->4->2->3->null.

<!--more-->

### Solution
* Time O(n)
* Split the list from the middle
* reverse the right list
* merge two lists and get the result
{% include_code LintCode/Reorder-List.py %}

