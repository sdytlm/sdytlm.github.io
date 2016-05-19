---
layout: post
title: "Palindrome Linked List"
date: 2016-05-13
comments: true
categories: LeetCode
tag: LeetCode
---

Given a singly linked list, determine if it is a palindrome.

#### Follow up
Could you do it in O(n) time and O(1) space?

<!--more-->
### Solution

* Use fast and slow point, then find the middle of the list
* Reverse right half and compare the left half and right half

{% include_code LeetCode/Python/Palindrome-Linked-List.py %}
