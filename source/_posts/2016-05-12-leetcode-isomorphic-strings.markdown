---
layout: post
title: "Isomorphic Strings"
date: 2016-05-12
comments: true
categories: LeetCode
tag: LeetCode
---


Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

#### Example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

#### Note
You may assume both s and t have the same length.


<!--more-->
### Solution
* Two hasmaps to record the map for s[i] and t[i]
* Judge if `sourceMap[s[i]] == t[i] and targetmap[t[i]] == s[i]`

{% include_code LeetCode/Python/Isomorphic-Strings.py %}
