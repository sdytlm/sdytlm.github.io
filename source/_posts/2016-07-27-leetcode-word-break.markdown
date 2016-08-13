---
layout: post
title: "Binary Tree Zigzag Level Order Traversal"
date: 2016-07-27
comments: true
categories: LeetCode
tag: LeetCode
---

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given

s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

<!--more-->
### Solution

假设dp(i)表示长度为i的字串能否别切分，dp方程如下:

`dp(i) = dp(j) && s[j, i) in dict`

{% include_code LeetCode/Python/Word-Break.py %}
