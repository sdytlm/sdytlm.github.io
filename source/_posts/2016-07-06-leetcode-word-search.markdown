---
layout: post
title: "Word Search"
date: 2016-07-06
comments: true
categories: LeetCode
tag: LeetCode
---



Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

#### Example
Given 
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
word = "ABCCED", -> returns true,

word = "SEE", -> returns true,

word = "ABCB", -> returns false.

<!--more-->
### Solution
* Java: board[i][j] ^= 256，把字母变成非法数字
{% include_code LeetCode/Java/Word-Search.java %}

* Python: Use "." to replace the board[i][j] when it is visited.
{% include_code LeetCode/Python/Word-Search.py %}
