---
layout: post
title: "Delete Digits"
date: 2016-01-29
comments: true
categories: LintCode
---

### Delete Digits

Given string A representative a positive integer which has N digits, remove any k digits of the number, the remaining digits are arranged according to the original order to become a new positive integer.

Find the smallest integer after remove k digits.

N <= 240 and k <= N,

#### Example

Given an integer A = "178542", k = 4

return a string "12"

<!--more-->

### Solution
* Time: O(n)
* From left to right, if A[i] <= stack.top() (some previous elements in A), need to pop the stack, until find the stack.top() < A[i]
* Insert the current A[i]. Must be careful the case when A[i] is '0' 


{% include_code LintCode/Delete-Digits.py %}
