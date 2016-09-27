---
layout: post
title: "Restore IP Addresses"
date: 2016-08-08
comments: true
categories: LeetCode
tag: LeetCode
---

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

#### For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

<!--more-->

### Solution
* 深度优先搜索

* Java
{% include_code LeetCode/Java/Restore-IP-Addresses.java %}

* Python
{% include_code LeetCode/Python/Restore-IP-Addresses.py %}
