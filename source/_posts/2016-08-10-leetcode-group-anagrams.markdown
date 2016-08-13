---
layout: post
title: "Group Anagrams"
date: 2016-08-10
comments: true
categories: LeetCode
tag: LeetCode
---




Given an array of strings, group anagrams together.

#### For example, 
given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:
```
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
#### Note: 
All inputs will be in lower-case.
<!--more-->

### Solution
* hash_map:<strs[i], 和strs[i] 互为anagrams的其他字符串组成的列表>

{% include_code LeetCode/Python/Group-Anagrams.py %}
