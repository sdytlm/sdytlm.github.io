---
layout: post
title: "Remove Duplicates from Sorted List II"
date: 2016-07-05
comments: true
categories: LeetCode
tag: LeetCode
---



Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

#### Example
Given 1->2->3->3->4->4->5, return 1->2->5.

Given 1->1->1->2->3, return 2->3.

<!--more-->
### Solution
* Java
{% include_code LeetCode/Java/Remove-Duplicates-from-Sorted-List2.java %}

* Python
* New list only contains the node without duplicates in the old list.
{% include_code LeetCode/Python/Remove-Duplicates-from-Sorted-List2.py %}
