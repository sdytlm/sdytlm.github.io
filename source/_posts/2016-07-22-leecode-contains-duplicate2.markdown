---
layout: post
title: "Contains Duplicate II"
date: 2016-07-22
comments: true
categories: LeetCode
tag: LeetCode
---

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

<!--more-->
### Solution

* Use hash_map [nums[i],i] to help
{% include_code LeetCode/Python/Contains-Duplicate2.py %}
