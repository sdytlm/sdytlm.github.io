---
layout: post
title: "Copy List with Random Pointer"
date: 2016-02-12
comments: true
categories: LintCode
tag: LintCode
---

### Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

#### Challenge
Could you solve it with O(1) space?

<!--more-->
### Solution
* Time: O(n), Space O(n)
* For each old node, use hash_map(old_node, new_node) to test if old_node.next and old_node.random exists in the new list.

{% include_code LintCode/Copy-List-With-Random-Pointer.py %}

* For the Space O(1) solution, you should firstly create all nodes and `new_nodes.random = old_nodes.random`. After that, you update the new_nodes.random

 
