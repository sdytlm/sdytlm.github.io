---
layout: post
title: "Delete Node in a Linked List"
date: 2016-07-12
comments: true
categories: LeetCode
tag: LeetCode
---


Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

<!--more-->
### Solution
* Assume: you don't need to know the list
* Just consider how to erase the node.
{% include_code LeetCode/Python/Delete-Node-in-A-Linked-List.py %}
