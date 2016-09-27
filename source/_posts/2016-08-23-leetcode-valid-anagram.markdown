---
layout: post
title: "Valid Anagram"
date: 2016-08-23
comments: true
categories: LeetCode
tag: LeetCode
---




Given two strings s and t, write a function to determine if t is an anagram of s.

#### For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

#### Note:
You may assume the string contains only lowercase alphabets.

#### Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

<!--more-->
### Solution
* 排序s,t, 看是否相同
{% include_code LeetCode/Python/Valid-Anagram.py %}

* Java solution: 利用hash_map存每个字母出现次数
{% include_code LeetCode/Java/Valid-Anagram.java %}
