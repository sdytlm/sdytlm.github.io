---
layout: post
title: "Linked List Cycle"
date: 2016-02-11
comments: true
categories: LintCode
tag: LintCode
---

### Linked List Cycle

`Given a linked list, determine if it has a cycle in it.`


#### Example
Given -21->10->4->5, tail connects to node index 1, return true

#### Challenge
Can you solve it without using extra space?

<!--more-->

### Solution
* Time: O(n)
* Fast_node (step twice) and slow_node (step once), if two nodes meet, there is cycle.

{% include_code LintCode/Linked-List-Cycle.py %}
