---
layout: post
title: "Two Strings Are Anagrams"
date: 2015-12-14
comments: true
categories: LintCode
tag: LintCode
---

### Two Strings Are Anagrams

`Write a method anagram(s,t) to decide if two strings are anagrams or not.`

#### Example

Given s="abcd", t="dcab", return true.

#### Challenge
O(n) time, O(1) extra space

<!-- more -->

### Solution

* Create an array `alphabet[256]` to record how many times does each character appear
* Count and record appearance of each character in **s and t**
* Check alpabet array to see if any character appears for odd times

{% include_code LintCode/Two-Strings-Are-Anagrams.py %}
