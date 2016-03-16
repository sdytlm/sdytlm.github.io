---
layout: post
title: "Wrod Ladder"
date: 2016-03-08
comments: true
categories: LintCode
tag: LintCode 
---

Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

1. Only one letter can be changed at a time
2. Each intermediate word must exist in the dictionary
 

#### Notice

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

#### Example
Given:
start = "hit"

end = "cog"

dict = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

<!--more-->
### Solution

* Time O(n)
* Use BFS and a special queue to solve this problem
{% include_code LintCode/Word-Ladder.py %}
