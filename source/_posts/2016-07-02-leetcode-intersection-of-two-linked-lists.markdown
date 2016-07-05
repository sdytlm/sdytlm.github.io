---
layout: post
title: "Intersection of Two Linked Lists"
date: 2016-07-02
comments: true
categories: LeetCode
tag: LeetCode
---

Write a program to find the node at which the intersection of two singly linked lists begins.


#### Example:
The following two linked lists:
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```
begin to intersect at node c1.


#### Notes:

* If the two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns.
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.

<!--more-->
### Solution

* 挪动较长的list. 保证headA 和 headB到末尾距离相同

* 同时挪动headA和headB，判断是否有重合
{% include_code LeetCode/Python/Intersection-of-Two-Linked-Lists.py %} 
