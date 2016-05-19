---
layout: post
title: "Rotate List"
date: 2016-05-12
comments: true
categories: LeetCode
tag: LeetCode
---

Given a list, rotate the list to the right by k places, where k is non-negative.

#### Example
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

<!--more-->

### Solution
* Find the new head
* Connect the old head into new head list

{% include_code LeetCode/Python/Rotate-List.py %}
