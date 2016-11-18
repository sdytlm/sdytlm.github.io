---
layout: post
title: "House Robber 2"
date: 2016-08-05
comments: true
categories: LeetCode
tag: LeetCode
---

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

<!--more-->
### Solution
* Java: 不用dp
{% include_code LeetCode/Java/House-Robber2.java %}

* Python: Consider two cases: nums[0] not used and nums[n-1] not used
{% include_code LeetCode/Python/House-Robber2.py %}
