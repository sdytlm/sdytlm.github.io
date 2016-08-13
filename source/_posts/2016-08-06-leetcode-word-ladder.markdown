---
layout: post
title: "Word Ladder"
date: 2016-08-06
comments: true
categories: LeetCode
tag: LeetCode
---

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

* Only one letter can be changed at a time
* Each intermediate word must exist in the word list

#### Example:
beginWord = "hit"

endWord = "cog"

wordList = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",

return its length 5.

#### Note:
* Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.

<!--more-->
### Solution
* BFS 用stack[word,val] 存当前word 修改一次能到达的所有word

{% include_code LeetCode/Python/Word-Ladder.py %}
